from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.urls import path
from django.shortcuts import redirect
from .models import GlobalSettings


@admin.register(GlobalSettings)
class GlobalSettingsAdmin(TranslatableAdmin):
    fieldsets = [
        ('Multi-language fields', {
            'fields': (
                "seo_title",
                "seo_description",
                "seo_keywords",
                "copyright_footer_text",
                "footer_text",
                "about_us",
                "terms_and_conditions",
                "privacy_policy",
                "our_vision",
                "our_mission",
            )
        }),
        ('Website elements', {
            'fields': (
                "logo",
                "favicon",
                "email",
                "telephone",
            )
        }),
    ]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('', self.admin_site.admin_view(self.redirect_to_edit_global_settings), name='globalsettings_redirect'),
        ]
        return custom_urls + urls

    def redirect_to_edit_global_settings(self, request):
        settings = GlobalSettings.load()
        return redirect(f'../globalsettings/{settings.id}/change')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(GlobalSettingsAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

