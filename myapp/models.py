# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib.auth.models import User as Usuario
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.template import loader
from django.template.defaultfilters import slugify

from notify.signals import notify
from .utils import unique_slug_generator
from .widgets import ColorPickerWidget
from tinymce.models import HTMLField

User = settings.AUTH_USER_MODEL

# Create your models here.
class Responsable(models.Model):
    responsable = models.CharField(max_length=250)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return '{}'.format(self.responsable)

class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)

class Diputacion(models.Model):
    nombre = models.CharField(max_length=250)
    font_color = ColorField(blank=True)
    slug = models.SlugField(max_length=250, unique=True, default=None, blank=True, null=True)

    def __unicode__(self):
        return '{}'.format(self.nombre)

    class Meta:
        ordering = ["nombre"]

    def save(self):
        self.slug = slugify(self.nombre)
        super(Diputacion, self).save()

    def get_absolute_url(self):
        return reverse('myapp:subvencion_by_category',
                       args=[self.slug])

class Generalitat(models.Model):
    nombre = models.CharField(max_length=250)
    font_color = ColorField(blank=True)
    slug = models.SlugField(max_length=250, unique=True, default=None, blank=True, null=True)

    def __unicode__(self):
        return '{}'.format(self.nombre)

    class Meta:
        ordering = ["nombre"]

    def save(self):
        self.slug = slugify(self.nombre)
        super(Generalitat, self).save()

    def get_absolute_url(self):
        return reverse('myapp:subvencion_by_category',
                       args=[self.slug])

class Gobierno(models.Model):
    nombre = models.CharField(max_length=250)
    font_color = ColorField(blank=True)
    slug = models.SlugField(max_length=250, unique=True, default=None, blank=True, null=True)

    def __unicode__(self):
        return '{}'.format(self.nombre)

    class Meta:
        ordering = ["nombre"]

    def save(self):
        self.slug = slugify(self.nombre)
        super(Gobierno, self).save()

    def get_absolute_url(self):
        return reverse('myapp:subvencion_by_category',
                       args=[self.slug])

class Estado(models.Model):
    etapa = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, default=None, blank=True, null=True)
    # info for colors from here: https://github.com/laktek/really-simple-color-picker/tree/master
    font_color = ColorField(blank=True)

    def __unicode__(self):
        return '{}'.format(self.etapa)

    class Meta:
        ordering = ["etapa"]

    def save(self):
        self.slug = slugify(self.etapa)
        super(Estado, self).save()

    def get_absolute_url(self):
        return reverse('myapp:subvencion_by_category',
                       args=[self.slug])

    def count_subsidies(self):
        return Subvencion.objects.filter(estado=self.etapa)

class Colectivo(models.Model):
    nombre = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, default=None, blank=True, null=True)

    def __unicode__(self):
        return '{}'.format(self.nombre)

    class Meta:
        ordering = ["nombre"]

    def save(self):
        self.slug = slugify(self.nombre)
        super(Colectivo, self).save()

    def get_absolute_url(self):
        return reverse('myapp:subvencion_by_category',
                       args=[self.slug])

class Subvencion(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    inicio = models.DateField(blank=True, null=True)
    fin = models.DateField(blank=True, null=True)
    responsable = models.ManyToManyField(Responsable, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, unique=True)

    nombre = models.TextField(blank=False, default="")
    procedimiento = models.TextField(blank=True,
                             help_text="Enlace para los bases")
    bases = models.TextField(blank=True,
                                 help_text="Enlace para la solicitud")
    observaciones = models.TextField(blank=True,
                                     help_text="Enlace para observaciones")

    ENTE_CHOICES = (
        ('DA', 'Diputación de Alicante'),
        ('GV', 'Generalitat Valenciana'),
        ('GE', 'Gobierno de España'),
    )

    ente = models.CharField(max_length=255, choices=ENTE_CHOICES, default=None)
    diputacion = models.ForeignKey(Diputacion, on_delete=models.CASCADE, default=None, blank=True, null=True)
    generalitat = models.ForeignKey(Generalitat, on_delete=models.CASCADE, default=None, blank=True, null=True)
    gobierno = models.ForeignKey(Gobierno, on_delete=models.CASCADE, default=None, blank=True, null=True)

    cuantia = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default="Estado")
    comentarios = HTMLField(blank=True)

    # Link y numero de expediente GESTIONA
    drive = models.TextField(blank=True,
                                help_text="Drive")
    gestiona_expediente = models.CharField(max_length=250,
                                           help_text="Número de expediente del Gestiona",
                                           default="-")
    se_relaciona_con = models.ManyToManyField('self', blank=True, default='')
    colectivo = models.ManyToManyField(Colectivo, blank=True)

    users_like = models.ManyToManyField(User, related_name='subsidies_liked', blank=True)

    class Meta:
        ordering = ["fin"]
        verbose_name = 'Subvencion'
        verbose_name_plural = "Subvenciones"

    def __unicode__(self):
        if self.fin == None:
            return '{}'.format(self.nombre)
        else:
            return '{} {}'.format(self.nombre, self.fin.strftime("%Y"))

    def get_absolute_url(self):
        return reverse('myapp:subvencion_detail',
                       args=[self.id, self.slug])

    def ente_verbose(self):
        return dict(Subvencion.ENTE_CHOICES)[self.ente]

    # def save(self, *args, **kwargs):
    #     super(Subvencion, self).save(*args, **kwargs)
    #     if not self.slug:
    #         self.slug = "0000" + str(self.id)

# Function that do something before the model is saved => save()
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    # Lo q slugify hace es si el titulo es: coche item 1
    # Lo devuelve como (con los guiones): tesla-item-1
    #instance.slug = slugify(instance.title)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_post_receiver, sender=Subvencion)

# Function that send email after create
# def send_email_created_updates(sender, instance, created, *args, **kwargs):
#     if created == True:
#         recievers = []
#         for user in Usuario.objects.all():
#             # if self.request.user.email != user.email:
#             recievers.append(user.email)
#
#         html_message = loader.render_to_string(
#             'myapp/subv_email_create.html',
#             {
#                 'name_actor': instance.user.username,
#                 'name_subv': instance.nombre,
#                 'object': instance,
#                 'created': created
#             }
#         )
#
#         users = Usuario.objects.all()
#         notify.send(instance.user, recipient_list=list(users), actor=instance.user,
#                     verb='subvención', obj=instance, target=instance, nf_type='crear')
#
#         send_mail('Gestión de subvenciones',
#                   '',
#                   instance.user.email,
#                   ['amosisa700@gmail.com','jctarbena@gmail.com'], #receivers
#                   html_message=html_message
#         )
#
# post_save.connect(send_email_created_updates, sender=Subvencion)
