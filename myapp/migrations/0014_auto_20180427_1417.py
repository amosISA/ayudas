# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-27 12:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20180423_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subvencion',
            old_name='bases',
            new_name='procedimiento',
        ),
    ]
