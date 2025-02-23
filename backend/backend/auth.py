import os

from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

@api_view(['GET', 'POST'])
def auth(request):
    return HttpResponse(request.session)
    return JsonResponse(request.session, safe=False)
    User = get_user_model()
    user = User.objects.get(username='admin')
    token, created = Token.objects.get_or_create(user=user)

    # return HttpResponse(request.user, 200)
    return HttpResponse(token.key, 200)
