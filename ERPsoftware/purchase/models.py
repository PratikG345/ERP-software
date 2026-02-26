from django.db import models
from masters.models import AccountMaster,ItemMaster,HSNCode,UOMMaster
from django.contrib.auth.models import User
from django.db.models import Sum
from decimal import Decimal, ROUND_HALF_UP
# Create your models here.

class PO_type(models.Model):
    PO_type = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return f"{self.PO_type}"

class PurchaseOrder(models.Model):
    po_date = models.DateField(auto_now_add=True)
    vendor = models.ForeignKey(AccountMaster, on_delete=models.PROTECT)
    po_type = models.ForeignKey(PO_type, on_delete=models.PROTECT)
    payment_terms = models.CharField(max_length=200, blank=True, null=True)
    transport = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="purchase_orders_created",
        null=True,
        blank=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="purchase_orders_updated",
        null=True,
        blank=True
    )

    @property
    def basic_amount(self):
        return self.lines.aggregate(total=Sum('basic_amount'))['total'] or 0

    @property
    def tax_amount(self):
        return self.lines.aggregate(total=Sum('tax_amount'))['total'] or 0

    @property
    def total_amount(self):
        return self.lines.aggregate(total=Sum('total_amount'))['total'] or 0
    
    def __str__(self):
        return f"PO-{self.id}"

    
class PurchaseOrderLine(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name="lines")
    item = models.ForeignKey(ItemMaster, on_delete=models.PROTECT)
    unit = models.ForeignKey(UOMMaster, on_delete=models.PROTECT)

    qty = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    igst_rate = models.DecimalField(max_digits=5, decimal_places=2,default= 0)

    basic_amount = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    
    def clean(self):
        self.unit = self.item.unit
        print("IGST FROM HSN:", self.item.hsncode.igst)
        self.igst_rate = self.item.hsncode.igst
        self.basic_amount = (self.qty * self.rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.tax_amount = ((self.basic_amount * self.igst_rate) / 100).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.total_amount = (self.basic_amount + self.tax_amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        
