# Generated by Django 2.2.24 on 2021-11-17 16:30

from django.db import migrations, models

import tinymce.models

import openforms.config.models
import openforms.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0009_auto_20211117_1349"),
    ]

    operations = [
        migrations.AlterField(
            model_name="globalconfiguration",
            name="confirmation_email_content",
            field=tinymce.models.HTMLField(
                default=openforms.config.models.get_confirmation_email_content,
                help_text="Content of the confirmation email message. Can be overridden on the form level",
                validators=[openforms.utils.validators.DjangoTemplateValidator()],
                verbose_name="content",
            ),
        ),
        migrations.AlterField(
            model_name="globalconfiguration",
            name="confirmation_email_subject",
            field=models.CharField(
                default=openforms.config.models.get_confirmation_email_subject,
                help_text="Subject of the confirmation email message. Can be overridden on the form level",
                max_length=1000,
                validators=[openforms.utils.validators.DjangoTemplateValidator()],
                verbose_name="subject",
            ),
        ),
    ]
