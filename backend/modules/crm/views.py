import os
import json

from accessify import protected, private

from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from .models import CrmStatus, CrmDeal
from .serializers import CrmStatusSerializer, CrmDealSerializer

from modules.main.models import UserField
from modules.main.serializers import UserFieldSerializer

from modules.crm.models import UtmCrmDeal
from modules.crm.serializers import UtmCrmDealSerializer


@api_view(['GET', 'POST', 'UPDATE', 'DELETE'])
def statuses(request):
    if (request.method == 'GET'):
        status = CrmStatus.objects.all()
        status_serializer = CrmStatusSerializer(status, many=True)
        return JsonResponse(status_serializer.data, safe=False)
    return JsonResponse([], safe=False)


class Deal:
    def __init__(self):
        pass

    @api_view(['GET', 'PUT'])
    def deal(request):
        if (request.method == 'GET'):
            deal = CrmDeal.objects.all()
            deal_serializer = CrmDealSerializer(deal, many=True)
            return JsonResponse(deal_serializer.data, safe=False)

        if (request.method == 'PUT'):
            deal_data = JSONParser().parse(request)

            if ('id' not in list(deal_data)):
                return JsonResponse({'result': False, 'message': 'Id not found!'}, status=status.HTTP_400_BAD_REQUEST)

            if ('data' not in list(deal_data)):
                return JsonResponse({'result': False, 'message': 'Data not found!'}, status=status.HTTP_400_BAD_REQUEST)

            deal = CrmDeal.objects.get(id=deal_data['id'])
            deal_serializer = CrmDealSerializer(deal, data=deal_data['data'], partial=True)

            if deal_serializer.is_valid():
                deal_serializer.save()
                print(deal_serializer.data)
                return JsonResponse(deal_serializer.data)
            return JsonResponse(deal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse([], safe=False)

    @api_view(['GET', 'POST', 'PUT', 'DELETE'])
    def deal_detail(request):
        if request.method == 'GET':
            if 'id' not in list(request.GET):
                return JsonResponse({'result': False, 'message': 'Id not found!'})

            pk = request.GET['id']
            deal = CrmDeal.objects.get(pk=pk)
            deal_data = CrmDealSerializer(deal).data

            # Для конкретного поля сделки получаем характеристики поля
            deal_fields_value = UtmCrmDeal.objects.all().prefetch_related('field').filter(deal_id=pk)
            deal_fields_value_serializer = UtmCrmDealSerializer(
                deal_fields_value, many=True)

            deal_fields = {}
            for user_field in deal_fields_value_serializer.data:
                if (user_field['field']['id'] not in deal_fields):
                    deal_fields[user_field['field']
                        ['id']] = user_field['field']
                    deal_fields[user_field['field']['id']]['values'] = []

                value = {**user_field}
                value.pop('field')

                deal_fields[user_field['field']['id']]['values'].append(value)

            deal_data['uf_list'] = list(deal_fields.values())

            # commit 2025-03-06
            # Получаем для конкретного поля все значения
            # user_fields = UserField.objects.prefetch_related('utm_crm_deals').all()
            # serializer = UserFieldSerializer(user_fields, many=True)
            # return Response(serializer.data)

            return JsonResponse(deal_data, safe=False)

        if (not request.data.get('id', 0)): 
            return JsonResponse({'result': False, 'message': 'Id not found!'}, status=status.HTTP_400_BAD_REQUEST)

        if (not request.data.get('data', None)):
            return JsonResponse({'result': False, 'message': 'Data not found!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            deal = CrmDeal.objects.get(id=request.data.get('id'))
        except CrmDeal.DoesNotExist:
            return Response({'error': 'Сделка не найдена'}, status=status.HTTP_404_NOT_FOUND)

        if (request.method == 'PUT'):
            deal_serializer = CrmDealSerializer(deal, data=request.data.get('data'), partial=True)
            if deal_serializer.is_valid():
                deal_serializer.save()  # Сохраняем основную сущность
                
                uset_field = request.data.get('data').get('uf_list', [])
                for field in uset_field:
                    for utm_value in field.get('values', []):
                        print(utm_value)
                        utm_id = utm_value.get('id')
                        if utm_id:
                            try:
                                utm_crm_deal = UtmCrmDeal.objects.get(id=utm_id)
                                print(utm_crm_deal, end='\n')
                                for attr, value in utm_value.items():
                                    if attr != 'deal':
                                        print(attr, value, end='\n')
                                        setattr(utm_crm_deal, attr, value)
                                utm_crm_deal.save()
                            except UtmCrmDeal.DoesNotExist:
                                pass
                        else:
                            pass
                            # # Если ID отсутствует, создаем новую запись TODO
                            # utm_crm_deal = UtmCrmDeal.objects.create(deal=crm_deal, **utm)
                            # utm_crm_deal.save()

                return Response(deal_serializer.data, status=status.HTTP_200_OK)

            return Response(deal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'DELETE':
            deal.delete()
            return JsonResponse({'result': True, 'message': 'Deal was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
    
        return JsonResponse([], safe=False)



class PageInit:
    def __init__(self):
        pass

    @api_view(['GET'])
    def crmDealInit(request, mode):
        deal = CrmDeal.objects.all()
        deal_serializer = CrmDealSerializer(deal, many=True)

        status = CrmStatus.objects.all()
        status_serializer = CrmStatusSerializer(status, many=True)

        unique_status = [status['status_id'] for status in status_serializer.data]

        response = {
            'entity': 'deal',
            'deals': deal_serializer.data,
            'status': status_serializer.data
        }

        if (mode == 'kanban'):
            response['stage_data'] = PageInit.prepareKanban(status_serializer.data, deal_serializer.data)

        return JsonResponse(response, safe=False)
        # return HttpResponse(str(unique_status), 200)
        
    def prepareKanban(status_list, entity_list):
        unique_status = [status['status_id'] for status in status_list]
        stage_data = {}
        
        for status_id in unique_status:
            stage_data[status_id] = {
                'status_data': {},
                'data': []
            }

            for status in status_list:
                if status['status_id'] == status_id:
                    stage_data[status_id]['status_data'] = status
                    break

            for deal in entity_list:
                if deal['stage_id'] == status_id:
                    stage_data[status_id]['data'].append(deal)

        stage_data = dict(sorted(stage_data.items(), key=lambda x: x[1]['status_data']['sort']))

        return stage_data