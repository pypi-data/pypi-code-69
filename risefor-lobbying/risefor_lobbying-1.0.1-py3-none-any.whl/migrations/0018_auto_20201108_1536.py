# Generated by Django 2.2.16 on 2020-11-08 15:36

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('risefor_lobbying', '0017_auto_20201004_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='subscriptionType',
            field=models.TextField(blank=True, verbose_name='Type de souscription'),
        ),
    ]
