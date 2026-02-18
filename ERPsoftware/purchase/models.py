from django.db import models
from masters.models import AccountMaster,ItemMaster,Unit,HSNCode

# Create your models here.

class PO_type(models.Model):
    PO_type = models.CharField(max_length=100,unique=True)

class PurchaseOrder(models.Model):
    po_date = models.DateField(auto_now_add=True)
    vendor = models.ForeignKey(AccountMaster, on_delete=models.PROTECT)
    po_type = models.ForeignKey(PO_type, on_delete=models.PROTECT)
    payment_terms = models.CharField(max_length=200, blank=True, null=True)
    transport = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"PO-{self.id}"

    
class PurchaseOrderLine(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name="lines")
    item = models.ForeignKey(ItemMaster, on_delete=models.PROTECT)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)

    qty = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    igst_rate = models.DecimalField(max_digits=5, decimal_places=2)

    basic_amount = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.basic_amount = self.qty * self.rate
        self.tax_amount = (self.basic_amount * self.igst_rate) / 100
        self.total_amount = self.basic_amount + self.tax_amount
        super().save(*args, **kwargs)
        