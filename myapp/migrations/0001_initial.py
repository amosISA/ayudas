# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-04 17:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diputacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('font_color', myapp.models.ColorField(blank=True, max_length=10)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etapa', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, default=None, max_length=250, null=True, unique=True)),
                ('font_color', myapp.models.ColorField(blank=True, max_length=10)),
            ],
            options={
                'ordering': ['etapa'],
            },
        ),
        migrations.CreateModel(
            name='Generalitat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('font_color', myapp.models.ColorField(blank=True, max_length=10)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Nombre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsable', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Subvencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField(blank=True, null=True)),
                ('fin', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('nombre', models.CharField(default='', max_length=250)),
                ('bases', models.TextField(blank=True, help_text='Enlace para las bases')),
                ('solicitud', models.TextField(blank=True, help_text='Enlace para la solicitud')),
                ('observaciones', models.TextField(blank=True, help_text='Enlace para observaciones')),
                ('ente', models.CharField(choices=[('DA', 'Diputaci\xf3n de Alicante'), ('GV', 'Generalitat Valenciana')], default=None, max_length=255)),
                ('cuantia', models.TextField(blank=True)),
                ('descripcion', models.TextField(blank=True)),
                ('comentarios', models.TextField(blank=True)),
                ('drive', models.TextField(blank=True, help_text='Drive')),
                ('gestiona_expediente', models.CharField(default='-', help_text='N\xfamero de expediente del Gestiona', max_length=250)),
                ('diputacion', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Diputacion')),
                ('estado', models.ForeignKey(default='Estado', on_delete=django.db.models.deletion.CASCADE, to='myapp.Estado')),
                ('generalitat', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Generalitat')),
                ('responsable', models.ManyToManyField(blank=True, to='myapp.Responsable')),
                ('se_relaciona_con', models.ManyToManyField(blank=True, default='', related_name='_subvencion_se_relaciona_con_+', to='myapp.Subvencion')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Subvencion',
                'verbose_name_plural': 'Subvenciones',
            },
        ),
    ]
