# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-22 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risefor_lobbying', '0010_auto_20200622_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actiongroup',
            name='twitterMessage',
            field=models.ManyToManyField(blank=True, related_name='twitterMessage', to='risefor_lobbying.TwitterMessage'),
        ),
    ]
