# Generated by Django 2.2.24 on 2021-10-27 15:43

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0006_globalconfiguration_payment_order_id_prefix"),
    ]

    operations = [
        migrations.AlterField(
            model_name="globalconfiguration",
            name="design_token_values",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                default=dict,
                help_text="Values of various style parameters, such as border radii, background colors... Note that this is advanced usage. Any available but un-specified values will use fallback default values. See https://open-forms.readthedocs.io/en/latest/installation/form_hosting.html#run-time-configuration for documentation.",
                verbose_name="design token values",
            ),
        ),
    ]
