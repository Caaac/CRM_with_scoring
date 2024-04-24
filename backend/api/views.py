from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from .models import Company

def jsonData(request):
    data = serialize('json', Company.objects.all())
    # return JsonResponse({'data': data})
    return HttpResponse(data, content_type='application/json')