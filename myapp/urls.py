"""bees_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ajaxdepartments/$', views.subsidies_for_ajax_loop, name='ajax_loop_departments'),
    url(r'^ajaxrelation/$', views.ajax_se_relaciona_con, name='ajax_se_relaciona_con'),
    url(r'^ajaxusers/$', views.ajax_users, name='ajax_get_users'),
    url(r'^like/$', views.subsidie_like, name='like'),
    url(r'^favourites/$', views.favourites, name='favourites'),
    url(r'^new/$', views.SubvencionCreateView.as_view(), name='new_subvencion'),
    url(r'^new/responsable/$', views.ResponsableCreateView.as_view(), name='new_responsable'),
    url(r'^new/diputacion/$', views.DiputacionCreateView.as_view(), name='new_diputacion'),
    url(r'^new/generalitat/$', views.GeneralitatCreateView.as_view(), name='new_generalitat'),
    url(r'^new/estado/$', views.EstadoCreateView.as_view(), name='new_estado'),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.SubvencionUpdateView.as_view(), name='edit_subvencion'),
    url(r'^delete/(?P<slug>[\w-]+)/$', views.SubvencionDeleteView.as_view(), name='delete_subvencion'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<estado_slug>[-\w ]+)/$', views.index, name='subvencion_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.subvencion_detail, name='subvencion_detail'),
]
