# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-27 12:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20180427_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subvencion',
            old_name='Solicitud',
            new_name='solicitud',
        ),
    ]
