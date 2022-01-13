import pytest

from ob_dj_survey.core.survey.models import SurveyAnswer, SurveyQuestion
from tests.core.survey.factories import (
    SurveyAnswerFactory,
    SurveyChoiceFactory,
    SurveyFactory,
    SurveyQuestionFactory,
    SurveyResponseFactory,
    SurveySectionFactory,
    UserFactory,
)


@pytest.mark.django_db
def test_user_model():
    """this will test the user factory"""
    instance = UserFactory(username="test user", email="admin@test.com",)
    assert instance.id
    assert instance.username
    assert instance.email


@pytest.mark.django_db
def test_survey_section_model():
    """this will test survey section model"""
    instance = SurveySectionFactory(
        name="Medical", description="description", meta={"test": "test"}
    )
    assert instance.id
    assert instance.name == "Medical"
    assert instance.description


@pytest.mark.django_db
def test_survey_model():
    """this will test survey model"""

    section = SurveySectionFactory(name="Medical", description="description")
    instance = SurveyFactory(callback="test_callback",)
    assert instance.id
    assert instance.callback


@pytest.mark.django_db
def test_question_model():
    """this will test question model"""

    section = SurveySectionFactory(name="Medical", description="description")
    survey = SurveyFactory(callback="test_callback",)
    instance = SurveyQuestionFactory(
        section=section,
        title="Which blood type do you have ?",
        type=SurveyQuestion.QuestionTypes.RADIO,
    )
    instance.surveys.set([survey])

    assert instance.id
    assert instance.surveys.all()
    assert instance.title == "Which blood type do you have ?"
    assert instance.type == SurveyQuestion.QuestionTypes.RADIO
    assert instance.section.pk == section.pk


@pytest.mark.django_db
def test_choice_model():
    """this will test choice model"""

    section = SurveySectionFactory(
        name="Medical", description="description", meta={"test": "test"}
    )
    survey = SurveyFactory(callback="test_callback", meta={"test": "test"})
    question = SurveyQuestionFactory(
        title="Which blood type do you have ?",
        type=SurveyQuestion.QuestionTypes.RADIO,
        section=section,
        meta={"test": "test"},
    )
    question.surveys.set([survey])
    instance_1 = SurveyChoiceFactory(title="O+", meta={"test": "test"})
    instance_1.questions.set([question])
    instance_2 = SurveyChoiceFactory(title="AB+", meta={"test": "test"})
    instance_2.questions.set([question])
    assert instance_1.id
    assert instance_2.id
    assert instance_1.title != instance_2.title
    assert instance_1.questions.all().first() == instance_2.questions.all().first()


@pytest.mark.django_db
def test_survey_response_model(user):
    """this will test survey response model"""

    section = SurveySectionFactory(
        name="Medical", description="description", meta={"test": "test"}
    )
    survey = SurveyFactory(callback="test_callback", meta={"test": "test"})
    question = SurveyQuestionFactory(
        title="Which blood type do you have ?",
        type=SurveyQuestion.QuestionTypes.RADIO,
        section=section,
        meta={"test": "test"},
    )

    question.surveys.set([survey])

    choice = SurveyChoiceFactory(title="O+", meta={"test": "test"})
    choice.questions.set([question])
    choice = SurveyChoiceFactory(title="AB+", meta={"test": "test"})
    choice.questions.set([question])
    instance = SurveyAnswerFactory(
        survey=survey,
        status=SurveyAnswer.Status.PARTIAL,
        created_by=user,
        meta={"test": "test"},
    )

    answer = SurveyResponseFactory(
        question=question, choice=choice, value=choice.title, meta={"test": "test"}
    )

    instance.responses.add(answer)

    assert instance.id
    assert instance.survey
    assert instance.status == SurveyAnswer.Status.PARTIAL
    assert instance.created_by == user
    assert instance.responses.all()
    record = instance.responses.first()
    assert record.question
    assert record.choice
    assert record.choice.title == record.value
