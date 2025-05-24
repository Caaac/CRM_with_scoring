import os
import json

from django.db import connection
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model, authenticate, logout

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes


# @api_view(['GET', 'POST'])
# def auth(request):
#     return HttpResponse(request.session)
#     return JsonResponse(request.session, safe=False)
#     User = get_user_model()
#     user = User.objects.get(username='admin')
#     token, created = Token.objects.get_or_create(user=user)

#     # return HttpResponse(request.user, 200)
#     return HttpResponse(token.key, 200)


# class Auth(APIView):
class Auth:
    def __init__(self):
        pass

    @csrf_exempt
    @staticmethod
    @api_view(['POST'])
    @permission_classes([AllowAny])
    def login(request):
        
        # data = request.data
        
        data = json.loads(request.body)
        login = data.get('login', None)
        password = data.get('password', None)

        print(1)

        if login is None or password is None:
            return Response({'status': 'error', 'message': 'login and password required'}, 400)

        print(2)
        # User = get_user_model()
        user = authenticate(username=login, password=password)

        if user is None:
            return Response({'status': 'error', 'message': 'uncorrect login or password'}, 400)
        print(3)
        refresh = RefreshToken.for_user(user)

        refresh.payload.update({
            'user_id': user.id,
            'username': user.login
        })
        print(4)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

        if login == 'admin' and password == 'qwerty1309':
            User = get_user_model()
            user = User.objects.get(username='admin')
            token, created = Token.objects.get_or_create(user=user)
            return HttpResponse(token.key, 200)
        else:
            return HttpResponse('1234', 200)

        # User = get_user_model()
        # user = User.objects.get(username='admin')
        # token, created = Token.objects.get_or_create(user=user)
        # return HttpResponse(token.key, 200)
