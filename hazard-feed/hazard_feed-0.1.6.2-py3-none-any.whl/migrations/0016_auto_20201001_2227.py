# Generated by Django 3.0.2 on 2020-10-01 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hazard_feed', '0015_auto_20200929_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hazardfeeds',
            old_name='link',
            new_name='external_link',
        ),
    ]
