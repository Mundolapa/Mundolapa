from django.db import models
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFieldsModel
from django.core.exceptions import ValidationError


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass


class GlobalSettings(SingletonModel, TranslatableModel):
    logo = models.ImageField(_("logo"), upload_to='images/logo/', blank=True, help_text=_("Upload website logo"))
    favicon = models.FileField(_("favicon"), upload_to='images/favicon/', blank=True,
                               help_text=_("Upload website favicon"))
    email = models.EmailField(_("email"), max_length=120, blank=True, null=True, help_text=_("Website email"))
    telephone = models.CharField(_("telephone"), max_length=120, blank=True, null=True,
                                 help_text=_("Website telephone"))

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)

    def save(self, *args, **kwargs):
        # Define the maximum size in bytes
        max_logo_size = 500 * 1024  # 500KB
        max_favicon_size = 50 * 1024  # 50KB

        if self.logo:
            if self.logo.file.size > max_logo_size:
                raise ValidationError("The logo file is too large ( > 500KB)")

        if self.favicon:
            if self.favicon.file.size > max_favicon_size:
                raise ValidationError("The favicon file is too large ( > 50KB)")

        super().save(*args, **kwargs)

    def __str__(self):
        return "Global Settings"

    class Meta:
        verbose_name = _("Global Settings")
        verbose_name_plural = _("Global Settings")


class GlobalSettingsTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(GlobalSettings, related_name='translations', on_delete=models.CASCADE)
    seo_title = models.CharField(_("title"), max_length=120, blank=True, null=True,
                                 help_text=_("Website SEO Title"))
    seo_description = models.TextField(_("description"), blank=True, null=True,
                                       help_text=_("Website SEO Description"))
    seo_keywords = models.CharField(_("keywords"), max_length=255, blank=True, null=True,
                                    help_text=_("Website SEO Keywords"))
    copyright_footer_text = models.CharField(_("copyright"), max_length=120, blank=True, null=True,
                                             help_text=_("Copyright Footer Text"))
    footer_text = models.TextField(_("footer text"), blank=True, null=True, help_text=_("Website Footer Text"))
    about_us = models.TextField(_("about us"), blank=True, null=True, help_text=_("About Us Text"))
    terms_and_conditions = models.TextField(_("terms and conditions"), blank=True, null=True,
                                            help_text=_("Terms And Conditions Text"))
    privacy_policy = models.TextField(_("privacy policy"), blank=True, null=True, help_text=_("Privacy Policy"))
    our_vision = models.TextField(_("our vision"), blank=True, null=True, help_text=_("Our Vision Text"))
    our_mission = models.TextField(_("our mission"), blank=True, null=True, help_text=_("Our Mission Text"))

    class Meta:
        unique_together = [('language_code', 'master', 'id')]
        indexes = [models.Index(fields=['id', 'language_code'])]
