# import another
from .classes.settings import UserFieldsListView, UserFieldDetailsView
from .classes.deal import DealDetail

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
                'sum_opportunity': 0,
                'data': []
            }

            for status in status_list:
                if status['status_id'] == status_id:
                    stage_data[status_id]['status_data'] = status
                    break

            for deal in entity_list:
                if deal['stage_id'] == status_id:
                    stage_data[status_id]['data'].append(deal)
                    stage_data[status_id]['sum_opportunity'] += int(deal['opportunity'] or 0)

        stage_data = dict(
            sorted(stage_data.items(), key=lambda x: x[1]['status_data']['sort']))

        return stage_data

