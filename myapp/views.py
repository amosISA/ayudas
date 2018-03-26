# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Count, Q
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import loader

from notify.signals import notify
from .models import Subvencion, Estado, Diputacion, Generalitat, Responsable, Gobierno
from .forms import SubvencionForm, ResponsableForm, DiputacionForm, GeneralitatForm, EstadoForm

# Create your views here.
####### AJAX REQUEST SE RELACIONA CON ######
def ajax_se_relaciona_con(request):
    diputacion = request.GET.getlist('diputacion_ajax[]', '99999')
    generalitat = request.GET.getlist('generalitat_ajax[]', '99999')
    gobierno = request.GET.getlist('gobierno_ajax[]', '99999')

    query = Subvencion.objects.all().filter(Q(diputacion__pk__in=diputacion) |
                                      Q(generalitat__pk__in=generalitat) |
                                      Q(gobierno__pk__in=gobierno))
    data = serializers.serialize('json', query)
    return HttpResponse(data, content_type="application/json")

def subsidies_for_ajax_loop(request):
    subvenciones = Subvencion.objects.all()
    diputacion = Diputacion.objects.all()
    generalitat = Generalitat.objects.all()
    gobierno = Gobierno.objects.all()

    return render(request,
                  'myapp/ajax_se_relaciona_con_modal.html',
                  {'subvenciones':subvenciones,
                   'diputacion':diputacion,
                   'generalitat':generalitat,
                   'gobierno':gobierno})

@login_required()
def index(request, estado_slug=None):
    estado = None
    diputacion = None
    generalitat = None
    gobierno = None
    user = None
    estados = Estado.objects.all().annotate(number_stats=Count('subvencion'))
    subvenciones = Subvencion.objects.all()
    total_subvenciones = Subvencion.objects.count()

    if estado_slug:
        if Diputacion.objects.filter(slug=estado_slug).exists():
            diputacion = get_object_or_404(Diputacion, slug=estado_slug)
            subvenciones = subvenciones.filter(diputacion=diputacion)
        elif Estado.objects.filter(slug=estado_slug).exists():
            estado = get_object_or_404(Estado, slug=estado_slug)
            subvenciones = subvenciones.filter(estado=estado)
        elif Generalitat.objects.filter(slug=estado_slug).exists():
            generalitat = get_object_or_404(Generalitat, slug=estado_slug)
            subvenciones = subvenciones.filter(generalitat=generalitat)
        elif Gobierno.objects.filter(slug=estado_slug).exists():
            gobierno = get_object_or_404(Gobierno, slug=estado_slug)
            subvenciones = subvenciones.filter(gobierno=gobierno)
        # To make it work for spaces in string(estado_slug=Juan Carlos) i modified url => r'^(?P<estado_slug>[-\w ]+)/$' => space in -\w
        elif Responsable.objects.filter(responsable=estado_slug).exists():
            user = get_object_or_404(Responsable, responsable=estado_slug)
            subvenciones = subvenciones.filter(responsable__responsable=user)
        else:
            subvenciones = Subvencion.objects.all()

    notification_list = request.user.notifications.active().prefetch()
    days_until_estado = ['7d', '6d', '5d', '4d', '3d', '2d', '1d', 'expires today', 'expired']

    return render(request,
                  'myapp/index.html',
                  {'estado': estado,
                   'diputacion': diputacion,
                   'generalitat': generalitat,
                   'gobierno': gobierno,
                   'user': user,
                   'estados': estados,
                   'subvenciones': subvenciones,
                   'days_until_estado': days_until_estado,
                   'notifications': notification_list,
                   'total_subvenciones': total_subvenciones})

@login_required()
def subvencion_by_user(request, name_slug):
    #Subvencion.objects.filter(responsable__responsable='Juan Carlos')
    subsidiers = None
    estados = Estado.objects.all().annotate(number_stats=Count('subvencion'))
    subvenciones = Subvencion.objects.all()

    if name_slug:
        subsidiers = get_object_or_404(Responsable, responsable=name_slug)
        subvenciones = subvenciones.filter(responsable__responsable=subsidiers)

    notification_list = request.user.notifications.active().prefetch()
    days_until_estado = ['7d', '6d', '5d', '4d', '3d', '2d', '1d', 'expires today', 'expired']

    return render(request,
                  'myapp/index.html',
                  {'subsidiers': subsidiers,
                   'estados': estados,
                   'subvenciones': subvenciones,
                   'days_until_estado': days_until_estado,
                   'notifications': notification_list})

@login_required()
def subvencion_detail(request, id, slug):
    subvencion = get_object_or_404(Subvencion,
                                   id=id,
                                   slug=slug)

    days_until_estado = ['7d', '6d', '5d', '4d', '3d', '2d', '1d', 'expires today', 'expired']

    return render(request,
                  'myapp/detail.html',
                  {'subvencion': subvencion,
                   'days_until_estado': days_until_estado})

# --------------- Create New Subsidie --------------- #
class SubvencionCreateView(LoginRequiredMixin, CreateView):
    form_class = SubvencionForm
    template_name = 'myapp/subvencion_create.html'
    success_url = reverse_lazy('myapp:index')

    def form_valid(self, form):
        # users = User.objects.exclude(username=self.request.user)

        # users = User.objects.all()
        # notify.send(self.request.user, recipient_list=list(users), actor=self.request.user,
        #             verb='subvención, %s' % (form.cleaned_data.get('nombre')), obj=form.instance, nf_type='crear')

        instance = form.save(commit=False)
        instance.user = self.request.user
        messages.success(self.request, 'Subvención añadida correctamente!')
        return super(SubvencionCreateView, self).form_valid(form)

# --------------- Edit Subsidie --------------- #
class SubvencionUpdateView(LoginRequiredMixin, UpdateView):
    model = Subvencion
    form_class = SubvencionForm
    template_name = 'myapp/subvencion_create.html'
    """
    fields = ["inicio", "fin", "responsable", "nombre", "bases", "solicitud", "observaciones", "ente",
            "diputacion", "generalitat", "cuantia", "descripcion", "estado", "comentarios", "drive",
            "gestiona_expediente", "se_relaciona_con"]
    """
    success_url = reverse_lazy('myapp:index')

    def form_valid(self, form):
        recievers = []
        for user in User.objects.all():
            # if self.request.user.email != user.email:
            recievers.append(user.email)

        users = User.objects.all()
        notify.send(self.request.user, recipient_list=list(users), actor=self.request.user,
                    verb='subvención', obj=form.instance, target=form.instance, nf_type='edit')

        object = form.instance
        html_message = loader.render_to_string(
            'myapp/subv_email_create.html',
            {
                'name_actor': self.request.user.username,
                'name_subv': form.cleaned_data.get('nombre'),
                'object': object
            }
        )

        send_mail('Gestión de subvenciones',
                  '',
                  self.request.user.email,
                  recievers,
                  html_message=html_message
        )

        messages.success(self.request, 'Subvención actualizada correctamente!')
        return super(SubvencionUpdateView, self).form_valid(form)

# --------------- Delete Subsidie --------------- #
class SubvencionDeleteView(LoginRequiredMixin, DeleteView):
    model = Subvencion
    success_url = reverse_lazy('myapp:index')

    def get_object(self, queryset=None):
        obj = super(SubvencionDeleteView, self).get_object()
        return obj

    def post(self, request, *args, **kwargs):
        if self.request.POST.get("confirm_delete"):
            # when confirmation page has been displayed and confirm button pressed
            recievers = []
            for user in User.objects.all():
                recievers.append(user.email)

            users = User.objects.all()
            notify.send(self.request.user, recipient_list=list(users), actor=self.request.user,
                        verb='subvención, %s' % (self.get_object()), nf_type='delete')

            self.get_object().delete()

            messages.success(self.request, 'Subvención eliminada correctamente!')
            return HttpResponseRedirect(self.success_url)
        elif self.request.POST.get("cancel"):
            # when confirmation page has been displayed and cancel button pressed
            return HttpResponseRedirect(reverse('myapp:index'))
        else:
            # when data is coming from the form which lists all items
            return self.get(self, *args, **kwargs)

# --------------- Create New Responsable --------------- #
class ResponsableCreateView(LoginRequiredMixin, CreateView):
    form_class = ResponsableForm
    template_name = 'myapp/responsable_create.html'

    def form_valid(self, form):
        recievers = []
        for user in User.objects.all():
            if self.request.user.email != user.email:
                recievers.append(user.email)

        users = User.objects.exclude(username=self.request.user)
        notify.send(self.request.user, recipient_list=list(users), actor=self.request.user,
                    verb='ha creado un nuevo responsable: "%s"' % (form.cleaned_data.get('responsable')), nf_type='crear')

        send_mail('Gestión de subvenciones',
                  '%s ha creado un nuevo responsable: "%s".' % (self.request.user.username, form.cleaned_data.get('responsable')),
                  self.request.user.email,
                  recievers)

        messages.success(self.request, 'Responsable añadido correctamente!')
        return super(ResponsableCreateView, self).form_valid(form)

    def get_success_url(self):
        url = self.request.GET.get('next')
        if url == '/new/':
            return reverse_lazy('myapp:new_subvencion')
        else:
            return reverse('myapp:edit_subvencion', kwargs={'slug': url[6:-1]})

# --------------- Create New Diputacion --------------- #
class DiputacionCreateView(LoginRequiredMixin, CreateView):
    form_class = DiputacionForm
    template_name = 'myapp/diputacion_create.html'
    success_url = reverse_lazy('myapp:new_subvencion')

    def form_valid(self, form):
        recievers = []
        for user in User.objects.all():
            if self.request.user.email != user.email:
                recievers.append(user.email)

        users = User.objects.exclude(username=self.request.user)
        notify.send(self.request.user, recipient_list=list(users), actor=self.request.user,
                    verb='ha creado un nuevo departameto: "%s"' % (form.cleaned_data.get('nombre')), nf_type='crear')

        send_mail('Gestión de subvenciones',
                  '%s ha creado un nuevo departamento (Diputación): "%s".' % (self.request.user.username, form.cleaned_data.get('nombre')),
                  self.request.user.email,
                  recievers)

        messages.success(self.request, 'Departamento (diputación) añadido correctamente!')
        return super(DiputacionCreateView, self).form_valid(form)

    def get_success_url(self):
        url = self.request.GET.get('next')
        if url == '/new/':
            return reverse_lazy('myapp:new_subvencion')
        else:
            return reverse('myapp:edit_subvencion', kwargs={'slug': url[6:-1]})

    # --------------- Create New Generalitat --------------- #
class GeneralitatCreateView(LoginRequiredMixin, CreateView):
    form_class = GeneralitatForm
    template_name = 'myapp/generalitat_create.html'
    success_url = reverse_lazy('myapp:new_subvencion')

    def form_valid(self, form):
        recievers = []
        for user in User.objects.all():
            if self.request.user.email != user.email:
                recievers.append(user.email)

        users = User.objects.exclude(username=self.request.user)
        notify.send(self.request.user, recipient_list=list(users), actor=self.request.user,
                    verb='ha creado un nuevo departamento: "%s"' % (form.cleaned_data.get('nombre')), nf_type='crear')

        send_mail('Gestión de subvenciones',
                  '%s ha creado un nuevo departamento (Generalitat): "%s".' % (self.request.user.username, form.cleaned_data.get('nombre')),
                  self.request.user.email,
                  recievers)

        messages.success(self.request, 'Departamento (generalitat) añadido correctamente!')
        return super(GeneralitatCreateView, self).form_valid(form)

    def get_success_url(self):
        url = self.request.GET.get('next')
        if url == '/new/':
            return reverse_lazy('myapp:new_subvencion')
        else:
            return reverse('myapp:edit_subvencion', kwargs={'slug': url[6:-1]})

# --------------- Create New Estado --------------- #
class EstadoCreateView(LoginRequiredMixin, CreateView):
    form_class = EstadoForm
    template_name = 'myapp/estado_create.html'
    success_url = reverse_lazy('myapp:new_subvencion')

    def form_valid(self, form):
        recievers = []
        for user in User.objects.all():
            if self.request.user.email != user.email:
                recievers.append(user.email)

        users = User.objects.exclude(username=self.request.user)
        notify.send(self.request.user, recipient_list=list(users), actor=self.request.user,
                    verb='ha creado un nuevo estado: "%s"' % (form.cleaned_data.get('etapa')), nf_type='crear')

        send_mail('Gestión de subvenciones',
                  '%s ha creado un nuevo estado: "%s".' % (self.request.user.username, form.cleaned_data.get('etapa')),
                  self.request.user.email,
                  recievers)

        messages.success(self.request, 'Estado añadido correctamente!')
        return super(EstadoCreateView, self).form_valid(form)

    def get_success_url(self):
        url = self.request.GET.get('next')
        if url == '/new/':
            return reverse_lazy('myapp:new_subvencion')
        else:
            return reverse('myapp:edit_subvencion', kwargs={'slug': url[6:-1]})