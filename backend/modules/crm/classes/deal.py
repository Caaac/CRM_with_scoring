from django.http import JsonResponse
from django.db.models import Prefetch

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from modules.main.models import UserField
from modules.main.serializers import UserFieldSerializer

from modules.crm.models import UtmCrmDeal, CrmDeal
from modules.crm.serializers import UtmCrmDealSerializer, CrmDealSerializer

class DealDetail(APIView):
  
    def get(self, request):
        if 'id' not in list(request.GET):
            return JsonResponse({'result': False, 'message': 'Id not found!'})
        
        if request.GET.get('id') == '0':
            return JsonResponse(self.getTemplate(fill=True), safe=False, status=status.HTTP_200_OK)
        
        pk = request.GET['id']
        
        try:
            deal = CrmDeal.objects.get(pk=pk)
        except CrmDeal.DoesNotExist:
            return JsonResponse({'result': False, 'message': 'Deal not found!'}, status=status.HTTP_404_NOT_FOUND)
        
        deal = CrmDeal.objects.get(pk=pk)
        deal_data = CrmDealSerializer(deal).data
        
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
            deal_fields[uf_value['field_id']]['values'].append(uf_value)
            
        for uf in deal_fields.values():
            value_tmpl = {
				"id": 0,
				"deal_id": pk,
				"field_id": uf['id'],
				"value": None,
				"value_int": None,
				"value_double": None,
				"value_datetime": None,
			}
            
            if (uf['user_type_id'] == 'enumirate'):
                deal_fields[uf['id']]['value_tmpl'] = value_tmpl
                
            if (not uf['values']):
                deal_fields[uf['id']]['values'] = [value_tmpl]
                
        deal_data['uf_list'] = list(deal_fields.values())

		# commit 2025-03-06
		# Получаем для конкретного поля все значения
		# user_fields = UserField.objects.prefetch_related('utm_crm_deals').all()
		# serializer = UserFieldSerializer(user_fields, many=True)
		# return Response(serializer.data)
        
        return JsonResponse(deal_data, safe=False)
    
    def post(self, request):    
        try:
            data = request.data.get('data', {})
            deal = CrmDealSerializer().create_from_detail(data)
            print(deal)
            return JsonResponse(
                {'status': 'success', 'data': deal}, 
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return JsonResponse(
                {'status': 'error', 'message': [str(e)]}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        

    def put(self, request):
        if (not request.data.get('id', 0)):
            return JsonResponse({'result': False, 'message': 'Id not found!'}, status=status.HTTP_400_BAD_REQUEST)

        if (not request.data.get('data', None)):
            return JsonResponse({'result': False, 'message': 'Data not found!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            deal = CrmDeal.objects.get(id=request.data.get('id'))
        except CrmDeal.DoesNotExist:
            return Response({'result': False, 'message': 'Deal not found!'}, status=status.HTTP_404_NOT_FOUND)
        
        deal_serializer = CrmDealSerializer(
                deal, data=request.data.get('data'), partial=True)
        if deal_serializer.is_valid():
            deal_serializer.save()

            uset_field = request.data.get('data').get('uf_list', [])
            for field in uset_field:
                for utm_value in field.get('values', []):
                    if not utm_value.get('value') \
                        and not utm_value.get('value_int') \
                        and not utm_value.get('value_double') \
                        and not utm_value.get('value_datetime'):
                        UtmCrmDeal.objects.filter(id=utm_value['id']).delete()
                    elif utm_id := utm_value.get('id'):
                        try:
                            utm_crm_deal = UtmCrmDeal.objects.get(
                                id=utm_id
                            )
                            for attr, value in utm_value.items():
                                if attr != 'deal':
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
    
    def delete(self, request):
        if (not request.data.get('id', 0)):
            return JsonResponse(
                {'result': False, 'message': 'Id not found!'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            deal = CrmDeal.objects.get(id=request.data.get('id'))
            deal.delete()
            return JsonResponse(
                {'result': True, 'message': 'Deal was deleted successfully!'}, 
                status=status.HTTP_204_NO_CONTENT
            )
        except CrmDeal.DoesNotExist:
            return Response(
                {'result': False, 'message': 'Deal not found!'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    
    def getTemplate(self, fill=False):
        result = CrmDealSerializer().getTemplate()
        uf = UserField.objects.filter(entity_id='DEAL').all()
        uf_list = []

        for uf_ser_data in UserFieldSerializer(uf, many=True).data:
            value = UtmCrmDealSerializer().getTemplate()
            value['field_id'] = uf_ser_data.get('id')
            uf_list.append({
                **uf_ser_data, 
                "values": [ value ]
            })    
            
        if fill:
            result['closed'] = 0
            result['is_new'] = 1
        
        result['uf_list'] = uf_list
        return result
    
    