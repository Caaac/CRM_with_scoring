from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Company, LandingRate, CrmDeal, Users
from .serializers import CompanySerializer, ContactSerializer, CrmDealSerializer, LandingRateSerializer, StatementSerializer, UsersSerializer

import logging
logger = logging.getLogger(__name__)

# CONSTANTS
from .api.settings import STAGES, SOURCE

from .banking_function.loan_profit import creditProfit

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
    
    
@api_view(['GET', 'PUT', 'DELETE'])    
def company_detail(request, pk):
    company = Company.objects.get(pk=pk)
    
    if request.method == 'GET': 
        company_serializer = CompanySerializer(company) 
        return JsonResponse(company_serializer.data)

    elif request.method == 'PUT': 
        company_data = JSONParser().parse(request) 
        company_serializer = CompanySerializer(company, data=company_data) 
        if company_serializer.is_valid(): 
            company_serializer.save() 
            return JsonResponse(company_serializer.data) 
        return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        company.delete() 
        return JsonResponse({'message': 'Company was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)





@api_view(['GET', 'POST', 'DELETE'])
def landing_rate_list(request):
    if request.method == 'GET':
        landingRate = LandingRate.objects.all()
        
        # for obj in landingRate:
        #     logger.info(f'Поля объекта с id {obj.id}: {obj.__dict__}')

        title = request.GET.get('title', None)
        print(title)
        if title is not None:
            landingRate = landingRate.filter(title__icontains=title)
        
        landingRate_serializer = LandingRateSerializer(landingRate, many=True)
        return JsonResponse(landingRate_serializer.data, safe=False)
        # 'safe=False' for objects serialization
        
        
        
        
        
@api_view(['GET', 'POST', 'DELETE'])
def crm_deal_list(request):
    if request.method == 'GET':
        crmDeal = CrmDeal.objects.all()
        
        title = request.GET.get('title', None)
        print(title)
        if title is not None:
            crmDeal = crmDeal.filter(title__icontains=title)
        
        crmDeal_serializer = CrmDealSerializer(crmDeal, many=True)
        return JsonResponse(crmDeal_serializer.data, safe=False)
        # 'safe=False' for objects serialization

from django.http import HttpResponse, JsonResponse
import json
@api_view(['GET', 'PUT', 'DELETE']) 
def crm_deal_detail(request, pk):
    crmDeal = CrmDeal.objects.get(pk=pk)
    
    if request.method == 'GET': 
        crmDeal_serializer = CrmDealSerializer(crmDeal) 
        return JsonResponse(crmDeal_serializer.data)

    elif request.method == 'PUT': 
        crmDeal_data = JSONParser().parse(request)
        
        if (crmDeal_data['loan_amount']):
            crmDeal_data['profit'] = creditProfit(crmDeal_data['loan_amount'], 0, 0)
        
        crmDeal_serializer = CrmDealSerializer(crmDeal, data=crmDeal_data) 
        
        # for key in crmDeal_data.keys():
        #     logger.info('1', crmDeal_data[str(key)])
        #     if crmDeal_data[key] == 'title':
        #         del crmDeal_data[key]
        # logger.info(crmDeal_data.keys())
        # logger.info(crmDeal_data['title'])
        # logger.info(creditProfit(crmDeal_data['loan_amount'], 0, 0))
        # logger.info(crmDeal_data)
        # return HttpResponse(crmDeal_data['title'])         
        
        if crmDeal_serializer.is_valid(): 
            crmDeal_serializer.save() 
            return JsonResponse(crmDeal_serializer.data) 
        return JsonResponse(crmDeal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        crmDeal.delete() 
        return JsonResponse({'message': 'CrmDeal was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET', 'PUT', 'DELETE']) 
# def crm_deal_detail(request, pk):
#     crmDeal = CrmDeal.objects.get(pk=pk)
#     crmDeal_data = JSONParser().parse(request) 
#     crmDeal_serializer = CrmDealSerializer(crmDeal, data=crmDeal_data) 
    
#     if crmDeal_serializer.is_valid(): 
#         crmDeal_serializer.save() 
#         return JsonResponse(crmDeal_serializer.data) 
#     return JsonResponse(crmDeal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']) 
def managers_list(request):
    menegers = Users.objects.all()
    
    if request.method == 'GET': 
        menegers_serializer = UsersSerializer(menegers, many=True) 
        return JsonResponse(menegers_serializer.data, safe=False)



def stages(request):
    return JsonResponse(STAGES, safe=False)

def source(request):
    return JsonResponse(SOURCE, safe=False)










from django.contrib.auth import authenticate
def test(request):
    # pass
    company = Company.objects.get(id=1)
    
    if request.method == 'GET': 
        company_serializer = CompanySerializer(company) 
        # return JsonResponse(company_serializer.data)
        # return JsonResponse(company_serializer.data)
    # return HttpResponse('1223', company)


















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

