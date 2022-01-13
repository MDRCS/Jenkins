import pytest
from django.urls import reverse
from rest_framework import status

from ob_dj_survey.apis.survey.serializers import SurveyAnswerSerializer
from ob_dj_survey.core.survey.models import SurveyAnswer, SurveyQuestion, SurveyResponse
from tests.core.survey.factories import (
    SurveyChoiceFactory,
    SurveyFactory,
    SurveyQuestionFactory,
    SurveySectionFactory,
)


@pytest.mark.django_db
def test_survey_answers__create(api_client, user):
    api_client.force_login(user)
    section = SurveySectionFactory(
        name="Medical", description="description", meta={"test": "test"}
    )
    survey = SurveyFactory(callback="test_callback", meta={"test": "test"})
    question_1 = SurveyQuestionFactory(
        title="Which blood type do you have ?",
        type=SurveyQuestion.QuestionTypes.RADIO,
        section=section,
        meta={"test": "test"},
    )
    question_1.surveys.set([survey])

    o_choice = SurveyChoiceFactory(title="O+", description="", meta={"test": "test"})
    o_choice.questions.set([question_1])

    ab_choice = SurveyChoiceFactory(
        title="AB+", description="AB+ blood type is rare.", meta={"test": "test"},
    )

    ab_choice.questions.set([question_1])
    question_2 = SurveyQuestionFactory(
        title="Which Type of Allergies do you have ?",
        type=SurveyQuestion.QuestionTypes.SELECT,
        section=section,
    )
    question_2.surveys.set([survey])
    milk_choice = SurveyChoiceFactory(
        title="Milk", description="Milk is a common allergy.",
    )
    milk_choice.questions.set([question_2])
    fish_choice = SurveyChoiceFactory(
        title="Fish", description="Fish is a common allergy.",
    )
    fish_choice.questions.set([question_2])
    question_3 = SurveyQuestionFactory(
        title="How Old Are You ?",
        type=SurveyQuestion.QuestionTypes.INTEGER,
        section=section,
    )
    question_3.surveys.set([survey])

    question_4 = SurveyQuestionFactory(
        title="How Old Are You ?",
        type=SurveyQuestion.QuestionTypes.FLOAT,
        section=section,
    )
    question_4.surveys.set([survey])
    question_5 = SurveyQuestionFactory(
        title="How do you describe your health ON The last Months?",
        type=SurveyQuestion.QuestionTypes.TEXT,
        section=section,
    )
    question_5.surveys.set([survey])
    question_6 = SurveyQuestionFactory(
        title="Do you drink alcohol?",
        type=SurveyQuestion.QuestionTypes.YES_NO,
        section=section,
    )
    question_6.surveys.set([survey])
    question_7 = SurveyQuestionFactory(
        title="Date of your last appointment with a Doctor?",
        type=SurveyQuestion.QuestionTypes.DATE,
        section=section,
    )
    question_7.surveys.set([survey])
    payload = {
        "survey": survey.pk,
        "answers": [
            {"question": question_1.pk, "choices": [ab_choice.pk]},
            {
                "question": question_2.pk,
                "choices": [fish_choice.pk],
                "values": ["Gluten"],
            },
            {"question": question_3.pk, "values": ["13"]},
            {"question": question_4.pk, "values": ["50.3"]},
            {
                "question": question_5.pk,
                "values": [
                    "Lorem Ipsum is simply dummy text of the printing and "
                    "typesetting industry. Lorem Ipsum has been the industry's "
                    "standard dummy text ever since the 1500s, when an unknown "
                    "printer took a galley of type and scrambled it to make a "
                    "type specimen book"
                ],
            },
            {"question": question_6.pk, "values": ["no"]},
            {"question": question_7.pk, "values": ["16-10-2021"]},
        ],
    }
    response = api_client.post(reverse("survey:survey-answers"), data=payload,)
    assert response.status_code == status.HTTP_201_CREATED
    assert SurveyAnswer.objects.count() == 1
    survey_answer = SurveyAnswer.objects.first()
    survey_data = SurveyAnswerSerializer(survey_answer).data
    assert survey_data == response.json()
    assert len(response.json()["responses"]) == 8  # number of answers
    assert response.json()["status"] == SurveyAnswer.Status.COMPLETED

    payload = {
        "survey": survey.pk,
        "answers": [
            {"question": question_1.pk, "choices": [o_choice.pk]},
            {
                "question": question_2.pk,
                "choices": [milk_choice.pk],
                "values": ["Flowers"],
            },
            {"question": question_3.pk, "values": ["13"]},
            {"question": question_4.pk, "values": ["50.3"]},
            {
                "question": question_5.pk,
                "values": [
                    "Lorem Ipsum is simply dummy text of the printing and "
                    "typesetting industry. Lorem Ipsum has been the industry's "
                    "standard dummy text ever since the 1500s, when an unknown "
                    "printer took a galley of type and scrambled it to make a "
                    "type specimen book"
                ],
            },
            {"question": question_6.pk, "values": ["yes"]},
            {"question": question_7.pk, "values": ["22-07-2021"]},
        ],
    }
    response = api_client.post(reverse("survey:survey-answers"), data=payload,)
    assert response.status_code == status.HTTP_201_CREATED
    assert SurveyAnswer.objects.count() == 1
    assert len(response.json()["responses"]) == SurveyResponse.objects.count()
    assert response.json()["responses"][0]["question"]["id"] == question_1.pk
    assert response.json()["responses"][0]["value"] == o_choice.title
