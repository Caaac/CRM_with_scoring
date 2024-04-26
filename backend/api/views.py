from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from .models import Company
from .serializers import CompanySerializer, ContactSerializer, CrmDealSerializer, LandingRateSerializer, StatementSerializer, UsersSerializer

from rest_framework.decorators import api_view


# from django.http import HttpResponse, JsonResponse
# from django.core.serializers import serialize
# from django.utils.html import escape


@api_view(['GET', 'POST', 'DELETE'])
def company_list(request):
    # return HttpResponse(escape(repr(request.method)))
    if request.method == 'GET':
        companies = Company.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            companies = companies.filter(title__icontains=title)
        
        companies_serializer = CompanySerializer(companies, many=True)
        return JsonResponse(companies_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    
    elif request.method == 'POST':
        companies_data = JSONParser().parse(request)
        companies_serializer = CompanySerializer(data=companies_data)
        if companies_serializer.is_valid():
            companies_serializer.save()
            return JsonResponse(companies_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(companies_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Company.objects.all().delete()
        return JsonResponse({'message': '{} Companies were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    
def company_detail(request, pk):
    pass





















# from django.http import HttpResponse, JsonResponse
# from django.core.serializers import serialize

'''
Print request on page
'''
# from django.utils.html import escape
# def company(request):
#     return HttpResponse(escape(repr(request)))

# def company(request):
    # data = serialize('json', Company.objects.all())
    # return HttpResponse(data, content_type='application/json')
    # return JsonResponse({'data': data})

