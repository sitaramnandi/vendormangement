from django.contrib import admin
from vendor_management.models import *

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg')  # Correct field names


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'vendor', 'order_date', 'status')  # Columns to display in the list view
    search_fields = ('po_number', 'vendor__name')  # Search fields, allowing lookup by vendor name
    list_filter = ('status', 'vendor')  # Filters for the admin interface

class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')  # Fields to display in the list view
    search_fields = ('vendor__name',)  # Search by vendor name
    list_filter = ('vendor', 'date')  # Filter by vendor and date

# Register Vendor with custom admin configuration
admin.site.register(Vendor, VendorAdmin)

# Register PurchaseOrder with custom admin configuration
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)

# Register HistoricalPerformance with default admin configuration
admin.site.register(HistoricalPerformance)
