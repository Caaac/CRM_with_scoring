from rest_framework import serializers
from .models import CrmContact, CrmDeal, CrmFieldMulti, CrmStatus

        
class CrmContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrmContact
        fields = '__all__'

class CrmDealSerializer(serializers.ModelSerializer):
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
    