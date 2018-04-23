from django.shortcuts import get_object_or_404
from .models import Subvencion

def subsidienav(request):
    # if not request.resolver_match.kwargs:
    if request.path == '/' or request.path == '/new/' or request.path == '/favourites/':
        user = request.user
        qs = Subvencion.objects.filter(users_like__in=[user])
        if qs.exists():
            return {'settings': qs}
        else:
            return {'settings': ''}
    elif request.path == '/accounts/login/':
        return {'settings':''}
    else:
        if not request.resolver_match.kwargs:
            return {'settings': ''}
        else:
            parameter_slug = request.resolver_match.kwargs.get('slug')
            subsidienav = get_object_or_404(Subvencion, slug=parameter_slug)
            return {'subsidienav': subsidienav}


