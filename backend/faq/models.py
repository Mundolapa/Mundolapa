from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.fields import TranslatedField
from parler.models import TranslatableModel, TranslatedFieldsModel
from ordered_model.models import OrderedModel

from base.managers import OrderedTranslatableManager


class Question(OrderedModel, TranslatableModel):
    question = TranslatedField(any_language=True)
    public = models.BooleanField(_("public"), default=True, help_text=_("Is this question public?"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(editable=False, db_index=True)

    objects = OrderedTranslatableManager()

    def __str__(self):
        return self.safe_translation_getter("question", any_language=True)


class QuestionTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='translations')
    question = models.TextField(_("question"), help_text=_("Write your question"))
    answer = models.TextField(_("answer"), help_text=_("Write your answer to the question"))

    class Meta:
        unique_together = [('language_code', 'master', 'id')]
        indexes = [models.Index(fields=['id', 'language_code'])]

    def __str__(self):
        return self.question
