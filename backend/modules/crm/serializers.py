from rest_framework import serializers
from .models import CrmContact, CrmDeal, CrmFieldMulti, CrmStatus, UtmCrmContact, UtmCrmDeal

from modules.main.serializers import UserFieldSerializer
        
class CrmContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrmContact
        fields = '__all__'

class UtmCrmDealSerializer(serializers.ModelSerializer):
    field = UserFieldSerializer(read_only=True)
    
    class Meta:
        model = UtmCrmDeal
        fields = '__all__'    

class CrmDealSerializer(serializers.ModelSerializer):
    utm_crm_deal = UtmCrmDealSerializer(many=True, read_only=True)
    
    class Meta:
        model = CrmDeal
        fields = '__all__'

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
    
        