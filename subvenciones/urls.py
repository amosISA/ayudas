"""subvenciones URL Configuration

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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import logout_then_login

from . import views

urlpatterns = [
    url(r'^logout/', logout_then_login, name='logout'),
    #url(r'^register/$', views.RegisterView.as_view(), name="register"),
    url(r'^panel/', admin.site.urls),
    url(r'^', include('myapp.urls', namespace='myapp')),
    url(r'^accounts/login/', views.custom_login, {'template_name': 'login.html'}, name='login'),
    url(r'^notifications/', include('notify.urls', namespace='notifications')),
    url(r'^tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
