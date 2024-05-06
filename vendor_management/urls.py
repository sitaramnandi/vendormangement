from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PurchaseOrderViewSet,VendorPerformanceView,PurchaseOrderAcknowledgeView

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
        path('vendors/<int:pk>/performance/', VendorPerformanceView.as_view({'get': 'retrieve'})),  # Vendor performance endpoint
    path('purchase_orders/<int:pk>/acknowledge/', PurchaseOrderAcknowledgeView.as_view({'post': 'create'})),  # Purchase order acknowledgment endpoint
]
