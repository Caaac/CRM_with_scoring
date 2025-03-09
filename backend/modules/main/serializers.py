from rest_framework import serializers
from .models import UserField, UserFieldEnum, User, Option

# from modules.crm.serializers import UtmCrmDealSerializer
        
class UserFieldEnumSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFieldEnum
        fields = '__all__'
        
class UserFieldSerializer(serializers.ModelSerializer):
    # commit 2025-03-06   
    # utm_crm_deals = UtmCrmDealSerializer(many=True, read_only=True)
    user_field = UserFieldEnumSerializer(many=True, read_only=True)

    class Meta:
        model = UserField
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'    
    