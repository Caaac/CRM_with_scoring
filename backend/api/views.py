from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from .models import Contact

def jsonData(request):
    data = serialize('json', Contact.objects.all())
    # return JsonResponse({'data': data})
    return HttpResponse(data, content_type='application/json')