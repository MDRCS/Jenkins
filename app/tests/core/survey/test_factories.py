import pytest

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
def test_user_factory():
    instance = UserFactory()
    assert instance.id


@pytest.mark.django_db
def test_question_factory():
    instance = SurveyQuestionFactory()
    assert instance.id


@pytest.mark.django_db
def test_survey_factory():
    instance = SurveyFactory()
    assert instance.id


@pytest.mark.django_db
def test_choice_factory():
    instance = SurveyChoiceFactory()
    assert instance.id


@pytest.mark.django_db
@pytest.mark.skip
def test_survey_response_factory():
    instance = SurveyResponseFactory()
    assert instance.id


@pytest.mark.django_db
def test_survey_section_factory():
    instance = SurveySectionFactory()
    assert instance.id


@pytest.mark.django_db
def test_survey_answer_factory():
    instance = SurveyAnswerFactory()
    assert instance.id
