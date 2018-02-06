# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import Subvencion, Responsable, Estado, Diputacion, Generalitat

# Register your models here.
class SubvencionAdmin(admin.ModelAdmin):
    list_display = ['inicio', 'nombre', 'fin', 'cuantia',
                    'Responsable', 'estado', 'Gestiona', 'gestiona_expediente', 'user']
    list_filter = ['nombre', 'estado', 'generalitat', 'diputacion', 'responsable']
    search_fields = ('nombre',)
    empty_value_display = '-' # para los campos vacios se pone eso
    list_display_links = ('nombre',) # que campo aparece como un link para editar el registro
    #raw_id_fields = ["departamento"]
    prepopulated_fields = {'slug': ('nombre',)}
    show_full_result_count = True

    def Responsable(self, obj):
        return format_html('<br>'.join([str(i.responsable) for i in obj.responsable.all()]))
    def Bases(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>',
                           obj.bases,
                           obj.bases)
    def Solicitud(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>',
                           obj.solicitud,
                           obj.solicitud)
    def Observaciones(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>',
                           obj.observaciones,
                           obj.observaciones)
    def Gestiona(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>',
                           obj.drive,
                           obj.drive)

    Responsable.allow_tags = True
    Observaciones.allow_tags = True
    Solicitud.allow_tags = True
    Bases.allow_tags = True
    Gestiona.allow_tags = True

    class Media:
        js = ('/static/admin/js/assets_admin.js',)
admin.site.register(Subvencion, SubvencionAdmin)

class ResponsableAdmin(admin.ModelAdmin):
    pass
admin.site.register(Responsable, ResponsableAdmin)

class EstadoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('etapa',)}
admin.site.register(Estado, EstadoAdmin)

class DiputacionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Diputacion, DiputacionAdmin)

class GeneralitatAdmin(admin.ModelAdmin):
    pass
admin.site.register(Generalitat, GeneralitatAdmin)