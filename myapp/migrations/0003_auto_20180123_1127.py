# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-23 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180123_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subvencion',
            name='fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subvencion',
            name='inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
