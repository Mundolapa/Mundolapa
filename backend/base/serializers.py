from rest_framework import serializers

from .models import GlobalSettings


# from rest_framework.fields import SerializerMethodField


class GlobalSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = GlobalSettings
        fields = (
            'seo_title',
            'seo_description',
            'seo_keywords',
            'copyright_footer_text',
            'footer_text',
            'about_us',
            'terms_and_conditions',
            'privacy_policy',
            'our_vision',
            'our_mission',
            'logo',
            'favicon',
            'email',
            'telephone'
        )

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            third_party_api_keys = representation.pop('third_party_api_keys', {})

            for key, value in third_party_api_keys.items():
                representation[key] = value

            return representation
