# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-23 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20180220_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='diputacion',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=250, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='generalitat',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=250, null=True, unique=True),
        ),
    ]
