# -*- coding: utf-8 -*-
from django.contrib.auth.views import login
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from .forms import RegisterForm

# --------------- Login --------------- #
def custom_login(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('myapp:index'))
    else:
        return login(request, template_name='login.html')
    return login(request, *args, **kwargs)

# --------------- User Registration --------------- #
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("myapp:index")

    # if user is logged, redirect him
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return HttpResponseRedirect(reverse('myapp:index'))
        return super(RegisterView, self).dispatch(*args, **kwargs)

