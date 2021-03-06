# Generated by Django 2.2.24 on 2021-07-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stuf", "0004_auto_20210722_1826"),
    ]

    operations = [
        migrations.AddField(
            model_name="soapservice",
            name="endpoint_beantwoord_vraag",
            field=models.URLField(
                blank=True,
                help_text="Endpoint for synchronous request messages, usually '[...]/BeantwoordVraag'",
                verbose_name="endpoint BeantwoordVraag",
            ),
        ),
        migrations.AlterField(
            model_name="soapservice",
            name="endpoint_ontvang_asynchroon",
            field=models.URLField(
                blank=True,
                help_text="Endpoint for asynchronous messages, usually '[...]/OntvangAsynchroon'.",
                verbose_name="endpoint OntvangAsynchroon",
            ),
        ),
        migrations.AlterField(
            model_name="soapservice",
            name="endpoint_vrije_berichten",
            field=models.URLField(
                blank=True,
                help_text="Endpoint for synchronous free messages, usually '[...]/VerwerkSynchroonVrijBericht' or '[...]/VrijeBerichten'.",
                verbose_name="endpoint VrijeBerichten",
            ),
        ),
        migrations.AlterField(
            model_name="soapservice",
            name="url",
            field=models.URLField(
                blank=True,
                help_text="URL of the StUF service to connect to.",
                verbose_name="URL",
            ),
        ),
    ]
