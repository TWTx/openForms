# Generated by Django 2.2.26 on 2022-01-12 09:30

from django.db import migrations

from openforms.formio.utils import iter_components


def forwards_func(apps, schema_editor):
    FormDefinition = apps.get_model("forms", "FormDefinition")
    for form_definition in FormDefinition.objects.all():
        changed = False
        for component in iter_components(form_definition.configuration):
            if component["type"] == "file":
                image = component.get("image")
                of_ns = component.get("of")
                if not of_ns and isinstance(image, dict):
                    # we move the 'image' dict a level deeper into 'of' prefix
                    component["of"] = {"image": image}
                    # set the original 'image' property
                    component["image"] = False
                    changed = True

        if changed:
            form_definition.save()
            print(f"updated of.image for {form_definition}")


class Migration(migrations.Migration):
    dependencies = [
        ("forms", "0013_auto_20211220_1755"),
    ]

    operations = [
        migrations.RunPython(forwards_func, migrations.RunPython.noop),
    ]
