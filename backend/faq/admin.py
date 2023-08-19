from django.contrib import admin

from .models import Question
from ordered_model.admin import OrderedModelAdmin
from parler.admin import TranslatableAdmin
from django.utils.translation import gettext_lazy as _, get_language


@admin.register(Question)
class QuestionAdmin(OrderedModelAdmin, TranslatableAdmin):
    list_display = ['question', 'move_up_down_links']

    def title_current_language(self, obj):
        return obj.safe_translation_getter("question", language_code=get_language())

    title_current_language.short_description = _("question")
