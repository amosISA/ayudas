# -*- coding: utf-8 -*-
from django import forms
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper

from .models import Subvencion, Responsable, Diputacion, Generalitat, Estado, ColorField
from .sites import my_admin_site

class DiputacionForm(forms.ModelForm):
    class Meta:
        model = Diputacion
        fields = ["nombre", "font_color"]

class GeneralitatForm(forms.ModelForm):
    class Meta:
        model = Generalitat
        fields = ["nombre", "font_color"]

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ["etapa", "font_color"]

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = ['responsable']

class DateInput(forms.DateInput):
    input_type = 'date'

class SubvencionForm(forms.ModelForm):
    class Meta:
        model = Subvencion
        fields = '__all__'
        widgets = {
            'inicio': DateInput(),
            'fin': DateInput(),
            'diputacion': RelatedFieldWidgetWrapper(
                Subvencion._meta.get_field('diputacion').formfield().widget,
                Subvencion._meta.get_field('diputacion').rel,
                my_admin_site,
                can_add_related=True
            ),
            'generalitat': RelatedFieldWidgetWrapper(
                Subvencion._meta.get_field('generalitat').formfield().widget,
                Subvencion._meta.get_field('generalitat').rel,
                my_admin_site,
                can_add_related=True
            ),
            'estado': RelatedFieldWidgetWrapper(
                Subvencion._meta.get_field('estado').formfield().widget,
                Subvencion._meta.get_field('estado').rel,
                my_admin_site,
                can_add_related=True
            ),
            'responsable': RelatedFieldWidgetWrapper(
                Subvencion._meta.get_field('responsable').formfield().widget,
                Subvencion._meta.get_field('responsable').rel,
                my_admin_site,
                can_add_related=True
            ),
        }
        exclude = ('slug',)