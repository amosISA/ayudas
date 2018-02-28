# -*- coding: utf-8 -*-
from django import forms
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.db.models import Q

from .models import Subvencion, Responsable, Diputacion, Generalitat, Estado, ColorField, Gobierno
from .sites import my_admin_site

class DiputacionForm(forms.ModelForm):
    class Meta:
        model = Diputacion
        fields = ["nombre", "font_color"]

class GeneralitatForm(forms.ModelForm):
    class Meta:
        model = Generalitat
        fields = ["nombre", "font_color"]

class GobiernoForm(forms.ModelForm):
    class Meta:
        model = Gobierno
        fields = ["nombre", "font_color"]

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ["etapa", "font_color"]

class ResponsableForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = ['responsable']

#class DateInput(forms.DateInput):
 #   input_type = 'date'
  #  format = ['%Y-%m-%d']

class SubvencionForm(forms.ModelForm):
    class Meta:
        model = Subvencion
        fields = '__all__'
        widgets = {
            'inicio': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date'}),
            'fin': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date'}),
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
            'gobierno': RelatedFieldWidgetWrapper(
                Subvencion._meta.get_field('gobierno').formfield().widget,
                Subvencion._meta.get_field('gobierno').rel,
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
            'se_relaciona_con': forms.CheckboxSelectMultiple(),
            'responsable': forms.CheckboxSelectMultiple(),
        }
        exclude = ('slug',)

    # def __init__(self, *args, **kwargs):
    #     super(SubvencionForm, self).__init__(*args, **kwargs)
    #     # access object through self.instance...
    #     self.fields['se_relaciona_con'].queryset = Subvencion.objects.filter(Q(diputacion=self.instance.diputacion) |
    #                                                                          Q(generalitat=self.instance.generalitat))