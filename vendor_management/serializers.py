from rest_framework import serializers
from vendor_management.models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        # Validate to ensure correct status values
    def validate_status(self, value):
        if value not in ['Pending', 'Completed', 'Cancelled']:
            raise serializers.ValidationError("Invalid status")
        return value

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
