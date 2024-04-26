from rest_framework import serializers
from .models import Company, Contact, CrmDeal, LandingRate, Statement, Users

        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class CrmDealSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrmDeal
        fields = '__all__'

class LandingRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingRate
        fields = '__all__'

class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = '__all__'
        
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'    
    