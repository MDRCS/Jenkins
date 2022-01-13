from __future__ import annotations

import factory.fuzzy
from django.contrib.auth import get_user_model

from ob_dj_survey.core.survey.models import (
    Survey,
    SurveyAnswer,
    SurveyChoice,
    SurveyQuestion,
    SurveyResponse,
    SurveySection,
)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()


class SurveySectionFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    description = factory.Faker("text")
    meta = factory.Faker("json")

    class Meta:
        model = SurveySection

    def __new__(cls, *args, **kwargs) -> SurveySectionFactory.Meta.model:
        return super().__new__(*args, **kwargs)


class SurveyFactory(factory.django.DjangoModelFactory):
    callback = factory.Faker("url")
    meta = factory.Faker("json")

    class Meta:
        model = Survey

    def __new__(cls, *args, **kwargs) -> SurveyFactory.Meta.model:
        return super().__new__(*args, **kwargs)


class SurveyQuestionFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("name")
    section = factory.SubFactory(SurveySectionFactory)
    type = factory.fuzzy.FuzzyChoice(choices=SurveyQuestion.QuestionTypes.values)
    meta = factory.Faker("json")

    class Meta:
        model = SurveyQuestion

    def __new__(cls, *args, **kwargs) -> SurveyQuestionFactory.Meta.model:
        return super().__new__(*args, **kwargs)


class SurveyChoiceFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("name")
    description = factory.Faker("text")
    meta = factory.Faker("json")

    class Meta:
        model = SurveyChoice

    def __new__(cls, *args, **kwargs) -> SurveyChoiceFactory.Meta.model:
        return super().__new__(*args, **kwargs)


class SurveyResponseFactory(factory.django.DjangoModelFactory):
    question = factory.SubFactory(SurveyQuestionFactory)
    choice = factory.SubFactory(SurveyChoiceFactory)
    meta = factory.Faker("json")

    class Meta:
        model = SurveyResponse

    def __new__(cls, *args, **kwargs) -> SurveyResponseFactory.Meta.model:
        return super().__new__(*args, **kwargs)


class SurveyAnswerFactory(factory.django.DjangoModelFactory):
    survey = factory.SubFactory(
        SurveyFactory,
        questions=factory.RelatedFactoryList(SurveyQuestionFactory, size=3),
    )
    created_by = factory.SubFactory(UserFactory)
    status = factory.fuzzy.FuzzyChoice(choices=SurveyAnswer.Status.values)
    meta = factory.Faker("json")

    class Meta:
        model = SurveyAnswer

    def __new__(cls, *args, **kwargs) -> SurveyAnswerFactory.Meta.model:
        return super().__new__(*args, **kwargs)
