from datetime import datetime

from django.db import transaction

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from modules.main.models import UserField
from modules.main.serializers import UserFieldSerializer
from modules.crm.models import CrmContact, CrmDeal, CrmFieldMulti, CrmStatus, UtmCrmContact, UtmCrmDeal


class CrmContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrmContact
        fields = '__all__'


class UtmCrmDealSerializer(serializers.ModelSerializer):
    deal_id = serializers.PrimaryKeyRelatedField(
        source='deal', queryset=CrmDeal.objects.all())
    field_id = serializers.PrimaryKeyRelatedField(
        source='field', queryset=UserField.objects.all())
    field = UserFieldSerializer(read_only=True)

    class Meta:
        model = UtmCrmDeal
        fields = '__all__'
        extra_kwargs = {
            'id': {'required': False},
        }

    def __init__(self, *args, **kwargs):
        include_field = kwargs.pop('include_field', False)
        super(UtmCrmDealSerializer, self).__init__(*args, **kwargs)

        if not include_field:
            self.fields.pop('field')
            self.fields.pop('deal')
    
    def getTemplate(self):
        return { 'id': 0, **self.data }
    
    def valueNotEmpty(self, value):
        if len(value['value']) \
            or not value['value_int'] is None \
            or not value['value_double'] is None \
            or not value['value_datetime'] is None:
            return True
        
        return False
    
    def canSave(self, value):
        return self(value).is_valid() and self.valueNotEmpty(self(value).data)




class CrmDealSerializer(serializers.ModelSerializer):
    utm_crm_deal = UtmCrmDealSerializer(many=True, read_only=True)

    class Meta:
        model = CrmDeal
        fields = '__all__'
        
    def getTemplate(self):
        result = { 'id': 0, **self.data }
        result['stage_id'] = 'NEW'
        return result
    
    def create_from_detail(self, data):
        uf_list = []

        for uf_item in data.pop('uf_list', []):
            for value_item in uf_item.get('values', []):
                if UtmCrmDealSerializer().valueNotEmpty(value_item):
                    del value_item['id']
                    uf_list.append(value_item)

        data['date_create'] = data['date_modify'] = datetime.now()
        data['closed'] = 0
        data['is_new'] = 1

        print(data)

        try:
            with transaction.atomic():
                deal_ser = CrmDealSerializer(data=data)
                
                if (not deal_ser.is_valid()):
                    raise ValidationError(deal_ser.errors)
                
                deal = deal_ser.save()
                
                for item in uf_list:
                    item['deal_id'] = deal.id
                
                uf_ser = UtmCrmDealSerializer(data=uf_list, many=True)

                if (not uf_ser.is_valid()):
                    raise ValidationError(uf_ser.errors)
                
                uf_ser.save()
                
                print({"id": deal.id})
                
                return {"id": deal.id}
                
        except ValidationError as e:
            print('ValidationError', e)
            raise e
        except Exception as e:
            print('Exception', e)
            raise ValidationError(str(e))

        return {}



class CrmFieldMultiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrmFieldMulti
        fields = '__all__'


class CrmStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrmStatus
        fields = '__all__'


class UtmCrmContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtmCrmContact
        fields = '__all__'
