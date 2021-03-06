# Generated by Django 2.2.20 on 2021-07-12 08:58

import uuid

import django.db.models.deletion
from django.db import migrations, models

import privates.fields
import privates.storages

import openforms.submissions.models
import openforms.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("submissions", "0022_temporaryfileupload"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubmissionFileAttachment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    openforms.utils.fields.StringUUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="UUID"
                    ),
                ),
                (
                    "form_key",
                    models.CharField(max_length=255, verbose_name="form component key"),
                ),
                (
                    "content",
                    privates.fields.PrivateMediaFileField(
                        help_text="Content of the submission file attachment.",
                        storage=privates.storages.PrivateMediaFileSystemStorage(),
                        upload_to=openforms.submissions.models.submission_file_upload_to,
                        verbose_name="content",
                    ),
                ),
                (
                    "file_name",
                    models.CharField(
                        blank=True,
                        help_text="reformatted file name",
                        max_length=255,
                        verbose_name="file name",
                    ),
                ),
                (
                    "original_name",
                    models.CharField(
                        help_text="original uploaded file name",
                        max_length=255,
                        verbose_name="original name",
                    ),
                ),
                (
                    "content_type",
                    models.CharField(max_length=255, verbose_name="inhoudstype"),
                ),
                (
                    "created_on",
                    models.DateTimeField(auto_now_add=True, verbose_name="created on"),
                ),
                (
                    "submission_step",
                    models.ForeignKey(
                        help_text="SubmissionStep the file is attached to.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="submissions.SubmissionStep",
                        verbose_name="submission",
                    ),
                ),
                (
                    "temporary_file",
                    models.ForeignKey(
                        help_text="Temporary upload this file is sourced to.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="attachments",
                        to="submissions.TemporaryFileUpload",
                        verbose_name="temporary file",
                    ),
                ),
            ],
            options={
                "verbose_name": "submission file attachment",
                "verbose_name_plural": "submission file attachment",
            },
        ),
    ]
