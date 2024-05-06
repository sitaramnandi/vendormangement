from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, Vendor
from datetime import datetime

@receiver(post_save, sender=PurchaseOrder)
def update_delivery_metrics(sender, instance, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        on_time_pos = completed_pos.filter(delivery_date__gte=instance.delivery_date)
        vendor.on_time_delivery_rate = (on_time_pos.count() / completed_pos.count()) * 100

        successful_pos = completed_pos.filter(status='completed')
        vendor.fulfillment_rate = (successful_pos.count() / PurchaseOrder.objects.filter(vendor=vendor).count()) * 100
        
        vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_quality_rating_avg(sender, instance, **kwargs):
    if instance.status == 'completed' and instance.quality_rating is not None:
        vendor = instance.vendor
        completed_pos_with_rating = PurchaseOrder.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False)
        total_rating = sum(po.quality_rating for po in completed_pos_with_rating)
        vendor.quality_rating_avg = total_rating / completed_pos_with_rating.count()
        vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, **kwargs):
    if instance.acknowledgment_date:
        vendor = instance.vendor
        pos_with_acknowledgment = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
        total_response_time = sum((po.acknowledgment_date - po.issue_date).total_seconds() for po in pos_with_acknowledgment)
        vendor.average_response_time = total_response_time / pos_with_acknowledgment.count()
        vendor.save()
