# Generated by Django 2.2.20 on 2021-05-21 11:52

import uuid

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models

import openforms.utils.fields
import openforms.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ("submissions", "0015_delete_confirmationemailtemplate"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="submissionstep",
            options={
                "verbose_name": "Submission step",
                "verbose_name_plural": "Submission steps",
            },
        ),
        migrations.AlterField(
            model_name="submission",
            name="bsn",
            field=models.CharField(
                blank=True,
                default="",
                max_length=9,
                validators=[openforms.utils.validators.BSNValidator()],
                verbose_name="BSN",
            ),
        ),
        migrations.AlterField(
            model_name="submission",
            name="completed_on",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="completed on"
            ),
        ),
        migrations.AlterField(
            model_name="submission",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created on"),
        ),
        migrations.AlterField(
            model_name="submission",
            name="current_step",
            field=models.PositiveIntegerField(default=0, verbose_name="current step"),
        ),
        migrations.AlterField(
            model_name="submission",
            name="registration_result",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                help_text="Contains data returned by the registration backend while registering the submission data.",
                null=True,
                verbose_name="registration backend result",
            ),
        ),
        migrations.AlterField(
            model_name="submission",
            name="registration_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending (not registered yet)"),
                    ("success", "Success"),
                    ("failed", "Failed"),
                ],
                default="pending",
                help_text="Indication whether the registration in the configured backend was successful.",
                max_length=50,
                verbose_name="registration backend status",
            ),
        ),
        migrations.AlterField(
            model_name="submission",
            name="suspended_on",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="suspended on"
            ),
        ),
        migrations.AlterField(
            model_name="submission",
            name="uuid",
            field=openforms.utils.fields.StringUUIDField(
                default=uuid.uuid4, unique=True, verbose_name="UUID"
            ),
        ),
        migrations.AlterField(
            model_name="submissionstep",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created on"),
        ),
        migrations.AlterField(
            model_name="submissionstep",
            name="data",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, null=True, verbose_name="data"
            ),
        ),
        migrations.AlterField(
            model_name="submissionstep",
            name="modified",
            field=models.DateTimeField(auto_now=True, verbose_name="modified on"),
        ),
        migrations.AlterField(
            model_name="submissionstep",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, unique=True, verbose_name="UUID"
            ),
        ),
    ]
