from rest_framework import serializers
from .models import Property, CheckbookTransaction, ClientKPISettings, CapitalExpenditureForecast, VendorPerformance, TenantTicket

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class CheckbookTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckbookTransaction
        fields = '__all__'

class ClientKPISettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientKPISettings
        fields = '__all__'

class CapExForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapitalExpenditureForecast
        fields = '__all__'

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorPerformance
        fields = '__all__'

class TenantTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantTicket
        fields = '__all__'
