# Generated by Django 4.2.4 on 2023-08-11 22:51

from django.db import migrations, models
import django.db.models.deletion
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='QuestionTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('question', models.TextField(help_text='Write your question', verbose_name='question')),
                ('answer', models.TextField(help_text='Write your answer to the question', verbose_name='answer')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='faq.question')),
            ],
            options={
                'indexes': [models.Index(fields=['id', 'language_code'], name='faq_questio_id_024bc5_idx')],
                'unique_together': {('language_code', 'master', 'id')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
