import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

from ob_dj_survey.apis.survey.serializers import SurveySerializer
from ob_dj_survey.core.survey.models import Survey
from tests.core.survey.factories import SurveyFactory, SurveyQuestionFactory


@pytest.mark.django_db
def test_survey_listing_has_no_permission(api_client, user):
    api_client.force_login(user)
    survey = SurveyFactory()
    instance = SurveyQuestionFactory(is_active=True)
    instance.surveys.set([survey])
    response = api_client.get(reverse("survey:survey-list"))
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_survey_listing_ok(monkeypatch, api_client, user):
    def can_manage_surveys_mck(self, request, view):
        return True

    monkeypatch.setattr(
        User, "can_manage_surveys", can_manage_surveys_mck, raising=False
    )

    api_client.force_login(user)
    survey = SurveyFactory()
    instance = SurveyQuestionFactory(is_active=True)
    instance.surveys.set([survey])

    response = api_client.get(reverse("survey:survey-list"))
    assert response.status_code == status.HTTP_200_OK
    assert Survey.objects.count() == 1
    survey = SurveySerializer(survey).data
    assert survey in response.json()["results"]
    assert "name" in response.json()["results"][0]
