import graphene
from graphene_django.types import DjangoObjectType
from .models import Question, QuestionTranslation


class QuestionTranslationType(DjangoObjectType):
    class Meta:
        model = QuestionTranslation
        fields = ('question', 'answer', 'language_code', 'master')


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('public', 'created', 'updated', 'order', 'translations')


class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionTranslationType)
    question = graphene.Field(QuestionType, id=graphene.Int(required=True))

    def resolve_all_questions(self, info, **kwargs):
        return QuestionTranslation.objects.select_related("master").all()

    def resolve_question(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Question.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
