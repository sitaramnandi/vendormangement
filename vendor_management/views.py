from rest_framework import viewsets,status
from vendor_management.models import Vendor, PurchaseOrder
from vendor_management.serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication

class VendorPerformanceView(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        try:
            vendor = Vendor.objects.get(pk=pk)  # Get the vendor by primary key
            # Return performance metrics
            data = {
                'on_time_delivery_rate': vendor.on_time_delivery_rate,
                'quality_rating_avg': vendor.quality_rating_avg,
                'average_response_time': vendor.average_response_time,
                'fulfillment_rate': vendor.fulfillment_rate,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Vendor.DoesNotExist:
            return Response({"detail": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)

class PurchaseOrderAcknowledgeView(viewsets.ViewSet):
    def create(self, request, pk=None):
        try:
            po = PurchaseOrder.objects.get(pk=pk)  # Get the purchase order by primary key
            po.acknowledgment_date = timezone.now()  # Update acknowledgment date
            po.save()  # Save changes
            return Response({"detail": "Purchase order acknowledged"}, status=status.HTTP_200_OK)
        except PurchaseOrder.DoesNotExist:
            return Response({"detail": "Purchase order not found"}, status=status.HTTP_404_NOT_FOUND)
