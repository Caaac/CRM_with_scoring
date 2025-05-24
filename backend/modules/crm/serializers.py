from rest_framework import serializers
from .models import CrmContact, CrmDeal, CrmFieldMulti, CrmStatus, UtmCrmContact, UtmCrmDeal

from modules.main.serializers import UserFieldSerializer


class CrmContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrmContact
        fields = '__all__'


class UtmCrmDealSerializer(serializers.ModelSerializer):
    deal_id = serializers.PrimaryKeyRelatedField(
        source='deal', queryset=CrmDeal.objects.all())
    field_id = serializers.PrimaryKeyRelatedField(
        source='field', queryset=UtmCrmDeal.objects.all())
    field = UserFieldSerializer(read_only=True)

    def __init__(self, *args, **kwargs):
        include_field = kwargs.pop('include_field', False)
        super(UtmCrmDealSerializer, self).__init__(*args, **kwargs)

        if not include_field:
            self.fields.pop('field')
            self.fields.pop('deal')

    # def create(self, deal, field, validated_data):

    class Meta:
        model = UtmCrmDeal
        fields = '__all__'
        extra_kwargs = {
            'id': {'required': False},
        }


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
