# Generated by Django 2.2.25 on 2021-12-17 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zgw_consumers", "0013_oas_field"),
        ("kvk", "0002_remove_kvkconfig_use_operation"),
    ]

    operations = [
        migrations.AddField(
            model_name="kvkconfig",
            name="profiles",
            field=models.OneToOneField(
                help_text="API used to retrieve basis profielen",
                limit_choices_to={"api_type": "orc"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="zgw_consumers.Service",
                verbose_name="KvK API Basisprofiel",
            ),
        ),
        migrations.AlterField(
            model_name="kvkconfig",
            name="service",
            field=models.OneToOneField(
                help_text="API used for validation of KvK, RSIN and vestigingsnummer's",
                limit_choices_to={"api_type": "orc"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="zgw_consumers.Service",
                verbose_name="KvK API Zoeken",
            ),
        ),
    ]
