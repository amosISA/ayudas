# -*- coding: utf-8 -*-
from django import forms

from .models import Subvencion, Responsable, Diputacion, Generalitat, Estado, ColorField

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
        fields = ["responsable"]

class DateInput(forms.DateInput):
    input_type = 'date'

class SubvencionForm(forms.ModelForm):
    class Meta:
        model = Subvencion
        fields = '__all__'
        widgets = {
            'inicio': DateInput(),
            'fin': DateInput()
        }
        exclude = ('slug',)