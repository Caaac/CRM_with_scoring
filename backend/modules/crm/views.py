import os
import json
import random
import string

from accessify import protected, private

from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.views import View

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
            deal_serializer = CrmDealSerializer(
                deal, data=deal_data['data'], partial=True)

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
            # deal_fields_value = UtmCrmDeal.objects.all().prefetch_related('field').filter(deal_id=pk)
            # deal_fields_value_serializer = UtmCrmDealSerializer(deal_fields_value, many=True)

            # deal_fields = {}
            # for user_field in deal_fields_value_serializer.data:
            #     if (user_field['field']['id'] not in deal_fields):
            #         deal_fields[user_field['field']
            #             ['id']] = user_field['field']
            #         deal_fields[user_field['field']['id']]['values'] = []

            #     value = {**user_field}
            #     value.pop('field')

            #     deal_fields[user_field['field']['id']]['values'].append(value)

            # deal_data['uf_list'] = list(deal_fields.values())

            user_fields = UserField.objects.filter(entity_id='DEAL').all()
            user_fields_serializer = UserFieldSerializer(
                user_fields, many=True)

            deal_fields_value = UtmCrmDeal.objects.filter(deal_id=pk).all()
            deal_fields_value_serializer = UtmCrmDealSerializer(
                deal_fields_value, many=True)

            deal_fields = {}

            for uf in user_fields_serializer.data:
                uf['values'] = []
                deal_fields[uf['id']] = uf

            for uf_value in deal_fields_value_serializer.data:
                # uf_value['field_id'] = uf_value['field']['id']
                # del uf_value['field']
                deal_fields[uf_value['field_id']]['values'].append(uf_value)
                # deal_fields[uf_value['field']['id']]['values'].append(uf_value)

            for uf in deal_fields.values():
                if (not uf['values']):
                    deal_fields[uf['id']]['values'] = [
                        {
                            "id": 0,
                            "deal_id": pk,
                            "field_id": uf['id'],
                            "value": None,
                            "value_int": None,
                            "value_double": None,
                            "value_datetime": None,
                        }
                    ]

            deal_data['uf_list'] = list(deal_fields.values())

            # print(deal_fields_value_serializer.data)

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
            deal_serializer = CrmDealSerializer(
                deal, data=request.data.get('data'), partial=True)
            if deal_serializer.is_valid():
                deal_serializer.save()

                uset_field = request.data.get('data').get('uf_list', [])
                for field in uset_field:
                    for utm_value in field.get('values', []):
                        # print(utm_value)
                        utm_id = utm_value.get('id')
                        if utm_id:
                            try:
                                utm_crm_deal = UtmCrmDeal.objects.get(
                                    id=utm_id
                                )
                                print(utm_crm_deal, end='\n')
                                for attr, value in utm_value.items():
                                    if attr != 'deal':
                                        print(attr, value, end='\n')
                                        setattr(utm_crm_deal, attr, value)
                                utm_crm_deal.save()
                            except UtmCrmDeal.DoesNotExist:
                                pass
                        else:
                            field_obj = UserField.objects.get(id=field['id'])
                            del utm_value['id']
                            utm_serializer = UtmCrmDeal(
                                deal=deal, field=field_obj, **utm_value)
                            utm_serializer.save()

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

        unique_status = [status['status_id']
                         for status in status_serializer.data]

        response = {
            'entity': 'deal',
            'deals': deal_serializer.data,
            'status': status_serializer.data
        }

        if (mode == 'kanban'):
            response['stage_data'] = PageInit.prepareKanban(
                status_serializer.data, deal_serializer.data)

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

        stage_data = dict(
            sorted(stage_data.items(), key=lambda x: x[1]['status_data']['sort']))

        return stage_data


class Settings:
    def __init__(self):
        pass

    @api_view(['GET'])
    def user_field_list(request):
        user_fields = UserField.objects.all()
        user_fields_serializer = UserFieldSerializer(user_fields, many=True)
        return JsonResponse(user_fields_serializer.data, safe=False)

        # user_fields = UserField.objects.prefetch_related('utm_crm_deals').all()
        # serializer = UserFieldSerializer(user_fields, many=True)
        # return Response(serializer.data)

    @api_view(['GET', 'PUT', 'POST', 'DELETE'])
    def user_field_detail(request):
        if request.method == 'GET':
            # Settings.user_field_detail_GET(request)
            try:
                if id := request.GET.get('field_name'):
                    user_fields = UserField.objects.get(field_name=id)
                elif id := request.GET.get('id'):
                    user_fields = UserField.objects.get(id=id)
                else:
                    return JsonResponse({'result': False, 'message': 'Field not found!'}, status=status.HTTP_400_BAD_REQUEST)

                user_fields_serializer = UserFieldSerializer(
                    user_fields, many=False)
                return JsonResponse(user_fields_serializer.data, safe=False)
            except UserField.DoesNotExist:
                return JsonResponse({'result': False, 'message': 'Field not found!'}, status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'PUT':
            data = JSONParser().parse(request)

            if ('id' not in data.keys()):
                return JsonResponse({'result': False, 'message': 'Id not found!'}, status=status.HTTP_400_BAD_REQUEST)

            user_fields_serializer = UserFieldSerializer(
                UserField.objects.get(id=data['id']), data=data, partial=True
            )

            if user_fields_serializer.is_valid():
                user_fields_serializer.save()
                return JsonResponse(user_fields_serializer.data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(user_fields_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'POST':
            data = JSONParser().parse(request)
            field_name = 'UF_'
            scope = {
                'CRM': ['DEAL'],
            }

            for key, value in scope.items():
                if data.get('entity_id') in value:
                    field_name += key + '_'

            while True:
                test_name = field_name + Settings.uf_index_generator().__next__()
                exists = UserField.objects.filter(
                    field_name=test_name).exists()
                if (not exists):
                    field_name = test_name
                    break

            data['field_name'] = field_name
            user_fields_serializer = UserFieldSerializer(data=data)

            if user_fields_serializer.is_valid():
                user_fields_serializer.save()
                return JsonResponse(
                    {
                        'status': 'success',
                        'data': user_fields_serializer.data,
                        'error': None,
                    },
                    safe=False,
                    status=status.HTTP_201_CREATED
                )
            return JsonResponse(
                {
                    'status': 'error',
                    'data': None,
                    'error': user_fields_serializer.errors,
                },
                safe=False,
                status=status.HTTP_400_BAD_REQUEST
            )

        if request.method == 'DELETE':
            data = JSONParser().parse(request)

            if ('id' not in data.keys()):
                return JsonResponse({'status': 'error', 'data': [], 'message': 'Id not found!'}, status=status.HTTP_400_BAD_REQUEST)

            user_filed = UserField.objects.get(id=data['id'])
            user_filed.delete()
            
            return JsonResponse({'status': 'success', 'data': [], 'message': []}, status=status.HTTP_204_NO_CONTENT)

        # if request.method == 'DELETE':
        #     user_fields = UserField.objects.get(id=request.GET.get('id'))
        #     user_fields.delete()
        #     return JsonResponse({'result': True, 'message': 'Field was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    def user_field_detail_GET(request):
        try:
            if id := request.GET.get('field_name'):
                user_fields = UserField.objects.get(field_name=id)
            elif id := request.GET.get('id'):
                user_fields = UserField.objects.get(id=id)
            else:
                return JsonResponse({'error': 'Поле не найдено'}, status=status.HTTP_404_NOT_FOUND)

            user_fields_serializer = UserFieldSerializer(
                user_fields, many=False)
            return JsonResponse(user_fields_serializer.data, safe=False)
        except UserField.DoesNotExist:
            return JsonResponse({'error': 'Поле не найдено'}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def uf_index_generator():
        while True:
            length = random.randint(10, 13)
            number = ''.join(random.choice(string.digits)
                             for _ in range(length))
            yield str(int(number))
