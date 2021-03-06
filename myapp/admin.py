# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.admin.options import ModelAdmin
from django.core.mail import send_mail
from django import forms
from django.utils.html import format_html
from .models import Subvencion, Responsable, Estado, Diputacion, Generalitat, Colectivo, Gobierno
from notify.signals import notify
from .sites import my_admin_site

# Register your models here.
def email_notify(request, form, message, name_field):
    # recievers = []
    # for user in User.objects.all():
    #     if request.user.email != user.email:
    #         recievers.append(user.email)

    #users = User.objects.exclude(username=request.user)
    users = User.objects.all()
    notify.send(request.user, recipient_list=list(users), actor=request.user,
                verb=message+', "%s"' % (form.cleaned_data.get(name_field)), nf_type='crear')

    # send_mail('Gestión de subvenciones',
    #           '{} '.format(request.user.username)+message+': "{}".'.format(form.cleaned_data.get(name_field)),
    #           request.user.email,
    #           recievers)

class SubvencionAdmin(admin.ModelAdmin):
    list_display = ['inicio', 'nombre', 'fin', 'cuantia',
                    'estado', 'Gestiona', 'gestiona_expediente', 'user']
    list_filter = ['nombre', 'estado', 'generalitat', 'diputacion', 'responsable', 'colectivo', 'gobierno']
    search_fields = ('nombre',)
    empty_value_display = '-' # para los campos vacios se pone eso
    list_display_links = ('nombre',) # que campo aparece como un link para editar el registro
    #raw_id_fields = ["departamento"]
    #prepopulated_fields = {'slug': ('nombre',)}
    show_full_result_count = True
    exclude = ('slug',)

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
    def Procedimiento(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>',
                           obj.procedimiento,
                           obj.procedimiento)
    def Gestiona(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>',
                           obj.drive,
                           obj.drive)

    Responsable.allow_tags = True
    Procedimiento.allow_tags = True
    Solicitud.allow_tags = True
    Bases.allow_tags = True
    Gestiona.allow_tags = True

    class Media:
        js = ('/static/admin/js/assets_admin.js',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(SubvencionAdmin, self).save_model(request, obj, form, change)
my_admin_site.register(Subvencion, SubvencionAdmin)
admin.site.register(Subvencion, SubvencionAdmin)

class ResponsableAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        email_notify(request, form, message='responsable', name_field='responsable')
        super(ResponsableAdmin, self).save_model(request, obj, form, change)
admin.site.register(Responsable, ResponsableAdmin)

class EstadoAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    #prepopulated_fields = {'slug': ('etapa',)}
    #readonly_fields = 'etapa'

    def save_model(self, request, obj, form, change):
        email_notify(request, form, message='estado', name_field='etapa')
        super(EstadoAdmin, self).save_model(request, obj, form, change)
admin.site.register(Estado, EstadoAdmin)

class DiputacionAdmin(admin.ModelAdmin):
    exclude = ('slug',)

    def save_model(self, request, obj, form, change):
        email_notify(request, form, message='departamento (Diputación)', name_field='nombre')
        super(DiputacionAdmin, self).save_model(request, obj, form, change)
admin.site.register(Diputacion, DiputacionAdmin)

class GeneralitatAdmin(admin.ModelAdmin):
    exclude = ('slug',)

    def save_model(self, request, obj, form, change):
        email_notify(request, form, message='departamento (Generalitat)', name_field='nombre')
        super(GeneralitatAdmin, self).save_model(request, obj, form, change)
admin.site.register(Generalitat, GeneralitatAdmin)

class GobiernoAdmin(admin.ModelAdmin):
    exclude = ('slug',)

    def save_model(self, request, obj, form, change):
        email_notify(request, form, message='departamento (Gobierno de España)', name_field='nombre')
        super(GobiernoAdmin, self).save_model(request, obj, form, change)
admin.site.register(Gobierno, GobiernoAdmin)

class ColectivoAdmin(admin.ModelAdmin):
    exclude = ('slug',)

    def save_model(self, request, obj, form, change):
        email_notify(request, form, message='colectivo', name_field='nombre')
        super(ColectivoAdmin, self).save_model(request, obj, form, change)
admin.site.register(Colectivo, ColectivoAdmin)
