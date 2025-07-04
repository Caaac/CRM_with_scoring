import os
import json
import random
import string

from accessify import protected, private
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny

from modules.main.models import UserField
from modules.main.serializers import UserFieldSerializer

from modules.main.models import UserFieldEnum
from modules.main.serializers import UserFieldEnumSerializer

from modules.crm.models import CrmStatus
from modules.crm.serializers import CrmStatusSerializer

class UserFieldsListView(APIView):
	def get(self, request):
		user_fields = UserField.objects.all()
		user_fields_serializer = UserFieldSerializer(user_fields, many=True)
		return JsonResponse(user_fields_serializer.data, safe=False)


class UserFieldDetailsView(APIView):
    def get(self, request):
        if id := request.GET.get('field_name'):
            user_fields = UserField.objects.get(field_name=id)
        elif id := request.GET.get('id'):
            user_fields = UserField.objects.get(id=id)
        else:
            return JsonResponse(
                {'result': False, 'message': 'Field not found!'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user_fields_serializer = UserFieldSerializer(user_fields, many=False)
        return JsonResponse(user_fields_serializer.data, safe=False)
    
    def put(self, request):
        data = JSONParser().parse(request)
        
        if ('id' not in data.keys()):
            return JsonResponse(
                {'result': False, 'message': 'Id not found!'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user_fields_serializer = UserFieldSerializer(
			UserField.objects.get(id=data['id']), data=data, partial=True
		)
		
        data_enum_ids = []
        uf_enum = UserFieldEnum.objects.filter(user_field_id=data['id'])
        for el in data.get('user_field', []):
            if id := el.get('id'):
                data_enum_ids.append(id)
                ufn_serialeizer = UserFieldEnumSerializer(
                    UserFieldEnum.objects.get(pk=id), 
                    data=el,
                )
                if ufn_serialeizer.is_valid():
                    ufn_serialeizer.save()
            else:
                ufn_serialeizer = UserFieldEnumSerializer(data=el)
                if ufn_serialeizer.is_valid():
                    data_enum_ids.append(ufn_serialeizer.save().id)
		
            for enum in uf_enum:
                if (enum.id not in data_enum_ids):
                    enum.delete()

        if user_fields_serializer.is_valid():
            user_fields_serializer.save()
            return JsonResponse(
                user_fields_serializer.data, 
                safe=False, 
                status=status.HTTP_200_OK
            )
        
        return JsonResponse(
            user_fields_serializer.errors, 
            safe=False, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def post(self, request):
        data = JSONParser().parse(request)
        prefix = 'UF_'
        field_name = prefix
        scope = { 'CRM': ['DEAL'] }

        for key, value in scope.items():
            if data.get('entity_id') in value:
                field_name += key + '_'

        while True:
            test_name = field_name + Helper.uf_index_generator().__next__()
            exists = UserField.objects.filter(
                field_name=test_name).exists()
            if not exists:
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
    
    def delete(self, request):
        data = JSONParser().parse(request)

        if ('id' not in data.keys()):
            return JsonResponse(
                {'status': 'error', 'data': [], 'message': 'Id not found!'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        user_filed = UserField.objects.get(id=data['id'])
        user_filed.delete()

        return JsonResponse(
            {'status': 'success', 'data': [], 'message': []}, 
            status=status.HTTP_204_NO_CONTENT
        )

class StageView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        stages = CrmStatus.objects
        
        if (entity_id := request.GET.get('entity_id', None)):
            stages = stages.filter(entity_id=entity_id)
        else:
            stages = stages.all()
        
        stages_serializer = CrmStatusSerializer(stages, many=True)
        
        return Response(stages_serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        if (not request.data.get('id', 0)):
            return JsonResponse({'result': False, 'message': 'Id not found!'}, status=status.HTTP_400_BAD_REQUEST)

        if (not request.data.get('data', None)):
            return JsonResponse({'result': False, 'message': 'Data not found!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = CrmStatus.objects.get(id=request.data.get('id'))
            ser = CrmStatusSerializer(instance, data=request.data.get('data'), partial=True)
        except CrmStatus.DoesNotExist:
            return Response({'result': False, 'message': 'Stage not found!'}, status=status.HTTP_404_NOT_FOUND)

        if ser.is_valid():
            ser.save()
            return Response({"status": "success", "data": ser.data}, status=status.HTTP_200_OK)
        else: 
            return Response({"status": "error", "message": ser.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        if (not request.data.get('data', None)):
            return JsonResponse({'result': False, 'message': 'Data not found!'}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.get('data')
        data['status_id'] = 'C_' + Helper.stage_index_generator().__next__()

        ser = CrmStatusSerializer(data=data, partial=True)

        if ser.is_valid():
            ser.save()
            return Response({"status": "success", "data": ser.data}, status=status.HTTP_201_CREATED)
        else: 
            return Response({"status": "error", "message": ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        if (not request.data.get('id', 0)):
            return JsonResponse({'result': False, 'message': 'Id not found!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            stage = CrmStatus.objects.get(id=request.data.get('id'))
            stage.delete()
            return JsonResponse({'status': 'success'}, status=status.HTTP_204_NO_CONTENT)
        except CrmStatus.DoesNotExist:
            return Response({'status': 'error', 'message': 'Stage not found!'}, status=status.HTTP_404_NOT_FOUND)

class Helper():
    @staticmethod
    def uf_index_generator():
        while True:
            length = random.randint(10, 13)
            number = ''.join(random.choice(string.digits)
                             for _ in range(length))
            yield str(int(number))
    
    @staticmethod
    def stage_index_generator():
        while True:
            length = random.randint(4, 7)
            number = ''.join(random.choice(string.digits)
                             for _ in range(length))
            yield str(int(number))
