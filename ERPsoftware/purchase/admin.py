from django.contrib import admin
from .models import PO_type,PurchaseOrder,PurchaseOrderLine
# Register your models here.
admin.site.register(PO_type)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderLine)