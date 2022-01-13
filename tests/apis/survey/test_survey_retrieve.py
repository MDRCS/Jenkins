import pytest
from django.urls import reverse
from rest_framework import status

from ob_dj_survey.apis.survey.serializers import SurveySerializer
from ob_dj_survey.core.survey.models import Survey
from tests.core.survey.factories import (
    SurveyChoiceFactory,
    SurveyFactory,
    SurveyQuestionFactory,
    SurveySectionFactory,
)


@pytest.mark.django_db
def test_get_survey_details(api_client, user):
    api_client.force_login(user)
    section = SurveySectionFactory(
        name="Medical", description="description", meta={"test": "test"}
    )
    survey = SurveyFactory(callback="test_callback", meta={"test": "test"})
    survey_questions = SurveyQuestionFactory(
        is_active=True, section=section, meta={"test": "test"}
    )
    survey_questions.surveys.set([survey])
    choice = SurveyChoiceFactory()
    choice.questions.set([survey_questions])
    response = api_client.get(reverse("survey:survey-detail", args=[survey.id]),)
    assert response.status_code == status.HTTP_200_OK
    assert Survey.objects.count() == 1
    survey = SurveySerializer(survey).data
    assert survey == response.json()
    assert "questions" in response.json()
    assert response.json()["questions"][0]["choices"]
