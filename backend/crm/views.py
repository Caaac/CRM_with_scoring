from django.shortcuts import render
import os
from django.db import connection
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from .models import CrmStatus
from .serializers import CrmStatusSerializer



@api_view(['GET', 'POST', 'UPDATE', 'DELETE'])
def status(request):
  if (request.method == 'GET'):
    status = CrmStatus.objects.all()
    status_serializer = CrmStatusSerializer(status, many=True)
    return JsonResponse(status_serializer.data, safe=False)
  return JsonResponse([], safe=False)
