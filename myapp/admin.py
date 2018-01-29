# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import Subvencion, Responsable, Estado, Diputacion, Generalitat, Nombre

# Register your models here.
class SubvencionAdmin(admin.ModelAdmin):
    list_display = ['inicio', 'nombre', 'fin', 'cuantia',
                    'Responsable', 'estado', 'Gestiona', 'gestiona_expediente', 'user']
    list_filter = ['nombre', 'estado']
    search_fields = ('nombre',)
    empty_value_display = '-' # para los campos vacios se pone eso
    list_display_links = ('nombre',) # que campo aparece como un link para editar el registro
    #raw_id_fields = ["departamento"]
    prepopulated_fields = {'slug': ('nombre',)}
    show_full_result_count = True

    # def Inicio(self, obj):
    #     return format_html('<br><br>'.join([str(i.inicio) for i in obj.inicio.all()]))
    # def Fin(self, obj):
    #     return format_html('<br><br>'.join([str(i.fin) for i in obj.fin.all()]))
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

    #Inicio.allow_tags = True
    #Fin.allow_tags = True
    Responsable.allow_tags = True
    Observaciones.allow_tags = True
    Solicitud.allow_tags = True
    Bases.allow_tags = True
    Gestiona.allow_tags = True

    class Media:
        js = ('/static/admin/js/assets_admin.js',)
admin.site.register(Subvencion, SubvencionAdmin)

# class InicioAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Inicio, InicioAdmin)
#
# class FinAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Fin, FinAdmin)

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

class NombreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Nombre, NombreAdmin)