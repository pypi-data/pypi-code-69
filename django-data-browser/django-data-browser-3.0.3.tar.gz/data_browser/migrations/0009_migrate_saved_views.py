# Generated by Django 2.2.16 on 2020-10-26 20:25

from django.db import migrations

from data_browser.migration_helpers import forwards_0009


def forwards(apps, schema_editor):
    View = apps.get_model("data_browser", "View")
    forwards_0009(View)


class Migration(migrations.Migration):
    dependencies = [("data_browser", "0008_view_limit")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
