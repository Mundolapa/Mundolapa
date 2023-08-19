# Generated by Django 4.2.4 on 2023-08-10 03:00

from django.db import migrations, models
import django.db.models.deletion
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, help_text='Upload website logo', upload_to='images/logo/', verbose_name='logo')),
                ('favicon', models.FileField(blank=True, help_text='Upload website favicon', upload_to='images/favicon/', verbose_name='favicon')),
                ('email', models.EmailField(blank=True, help_text='Website email', max_length=120, null=True, verbose_name='email')),
                ('telephone', models.CharField(blank=True, help_text='Website telephone', max_length=120, null=True, verbose_name='telephone')),
            ],
            options={
                'verbose_name': 'Global Settings',
                'verbose_name_plural': 'Global Settings',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GlobalSettingsTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('seo_title', models.CharField(blank=True, help_text='Website SEO Title', max_length=120, null=True, verbose_name='title')),
                ('seo_description', models.TextField(blank=True, help_text='Website SEO Description', null=True, verbose_name='description')),
                ('seo_keywords', models.CharField(blank=True, help_text='Website SEO Keywords', max_length=255, null=True, verbose_name='keywords')),
                ('copyright_footer_text', models.CharField(blank=True, help_text='Copyright Footer Text', max_length=120, null=True, verbose_name='copyright')),
                ('footer_text', models.TextField(blank=True, help_text='Website Footer Text', null=True, verbose_name='footer text')),
                ('about_us', models.TextField(blank=True, help_text='About Us Text', null=True, verbose_name='about us')),
                ('terms_and_conditions', models.TextField(blank=True, help_text='Terms And Conditions Text', null=True, verbose_name='terms and conditions')),
                ('privacy_policy', models.TextField(blank=True, help_text='Privacy Policy', null=True, verbose_name='privacy policy')),
                ('our_vision', models.TextField(blank=True, help_text='Our Vision Text', null=True, verbose_name='our vision')),
                ('our_mission', models.TextField(blank=True, help_text='Our Mission Text', null=True, verbose_name='our mission')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='base.globalsettings')),
            ],
            options={
                'indexes': [models.Index(fields=['id', 'language_code'], name='base_global_id_650fd3_idx')],
                'unique_together': {('language_code', 'master', 'id')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
