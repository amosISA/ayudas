# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Subvencion, Estado
from .forms import SubvencionForm, ResponsableForm, DiputacionForm, GeneralitatForm, EstadoForm, NombreForm

# Create your views here.
@login_required()
def index(request, estado_slug=None):
    estado = None
    estados = Estado.objects.all()
    queryset_list = Subvencion.objects.all()
    paginator = Paginator(queryset_list, 300)

    page = request.GET.get('page', 1)

    try:
        subvenciones = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        subvenciones = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        subvenciones = paginator.page(paginator.num_pages)

    if estado_slug:
        estado = get_object_or_404(Estado, slug=estado_slug)
        subvenciones = subvenciones.filter(estado=estado)

    days_until_estado = ['7d', '6d', '5d', '4d', '3d', '2d', '1d', 'expires today', 'expired']

    return render(request,
                  'myapp/index.html',
                  {'estado': estado,
                   'estados': estados,
                   'subvenciones': subvenciones,
                   'days_until_estado': days_until_estado})

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
        instance = form.save(commit=False)
        instance.user = self.request.user
        messages.success(self.request, 'Subvención añadida correctamente!')
        return super(SubvencionCreateView, self).form_valid(form)

# --------------- Edit Subsidie --------------- #
class SubvencionUpdateView(LoginRequiredMixin, UpdateView):
    model = Subvencion
    template_name = 'myapp/subvencion_create.html'
    fields = ["inicio", "fin", "responsable", "nombre", "bases", "solicitud", "observaciones", "ente",
            "diputacion", "generalitat", "cuantia", "descripcion", "estado", "comentarios", "drive",
            "gestiona_expediente"]
    success_url = reverse_lazy('myapp:index')

    def form_valid(self, form):
        messages.success(self.request, 'Subvención actualizada correctamente!')
        return super(SubvencionUpdateView, self).form_valid(form)

# --------------- Delete Subsidie --------------- #
class SubvencionDeleteView(LoginRequiredMixin, DeleteView):
    model = Subvencion
    success_url = reverse_lazy('myapp:index')

    #def get_object(self, queryset=None):
    """ Hook to ensure object is owned by request.user. """
        #obj = super(SubvencionDeleteView, self).get_object()
        #if not obj.user == self.request.user:
            #raise Http404
        #return obj

    def post(self, request, *args, **kwargs):
        if self.request.POST.get("confirm_delete"):
            # when confirmation page has been displayed and confirm button pressed
            self.get_object().delete()
            messages.success(self.request, 'Subvención eliminada correctamente!')
            return HttpResponseRedirect(self.success_url)
        elif self.request.POST.get("cancel"):
            # when confirmation page has been displayed and cancel button pressed
            return HttpResponseRedirect(reverse('myapp:index'))
        else:
            # when data is coming from the form which lists all items
            return self.get(self, *args, **kwargs)

# # --------------- Create New Inicio --------------- #
# class InicioCreateView(LoginRequiredMixin, CreateView):
#     form_class = InicioForm
#     template_name = 'myapp/inicio_create.html'
#     success_url = reverse_lazy('myapp:new_subvencion')
#
#     def form_valid(self, form):
#         messages.success(self.request, 'Inicio añadido correctamente!')
#         return super(InicioCreateView, self).form_valid(form)
#
# # --------------- Create New Fin --------------- #
# class FinCreateView(LoginRequiredMixin, CreateView):
#     form_class = FinForm
#     template_name = 'myapp/fin_create.html'
#     success_url = reverse_lazy('myapp:new_subvencion')
#
#     def form_valid(self, form):
#         messages.success(self.request, 'Fin añadido correctamente!')
#         return super(FinCreateView, self).form_valid(form)

# --------------- Create New Responsable --------------- #
class ResponsableCreateView(LoginRequiredMixin, CreateView):
    form_class = ResponsableForm
    template_name = 'myapp/responsable_create.html'

    def form_valid(self, form):
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
        messages.success(self.request, 'Estado añadido correctamente!')
        return super(EstadoCreateView, self).form_valid(form)

    def get_success_url(self):
        url = self.request.GET.get('next')
        if url == '/new/':
            return reverse_lazy('myapp:new_subvencion')
        else:
            return reverse('myapp:edit_subvencion', kwargs={'slug': url[6:-1]})

# --------------- Create New Nombre --------------- #
class NombreCreateView(LoginRequiredMixin, CreateView):
    form_class = NombreForm
    template_name = 'myapp/nombre_create.html'
    success_url = reverse_lazy('myapp:new_subvencion')

    def form_valid(self, form):
        messages.success(self.request, 'Nombre añadido correctamente!')
        return super(NombreCreateView, self).form_valid(form)

    def get_success_url(self):
        url = self.request.GET.get('next')
        if url == '/new/':
            return reverse_lazy('myapp:new_subvencion')
        else:
            return reverse('myapp:edit_subvencion', kwargs={'slug': url[6:-1]})


