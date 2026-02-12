from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from decimal import Decimal

# Create your models here.
class UOMMaster(models.Model):
    unit = models.CharField(max_length=10,blank=True)
    fullform = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return f"{self.unit}-{self.fullform}"
    
class State(models.Model):
    state = models.CharField(max_length=100,unique=True)
    state_code = models.CharField(max_length=2,unique=True)
    def __str__(self):
        return f"{self.state}"
    
class HSNCode(models.Model):
    hsn_code = models.CharField(
        max_length=8,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^(\d{2}|\d{4}|\d{6}|\d{8})$',
                message="HSN code must be of 2,4,6,8 digits.",
            )
        ]
    )
    description = models.TextField(blank=True,null=True)
    igst = models.DecimalField(max_digits=5,decimal_places=2)
    sgst = models.DecimalField(max_digits=5,decimal_places=2,editable=False)
    cgst = models.DecimalField(max_digits=5,decimal_places=2,editable=False)
    cess = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    
    def save(self,*args, **kwargs):
        if self.igst is not None:
            half_tax = self.igst/Decimal('2');
            self.cgst = half_tax;
            self.sgst = half_tax;
            
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.hsn_code}"
    
    
class SACCode(models.Model):
    sac_code = models.CharField(
        max_length=8,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[99]{4}$',
                message='SAC code must be of 6 digits.',
            )
        ]
        )
    description = models.TextField(blank=True,null=True)
    igst = models.DecimalField(max_digits=5,decimal_places=2)
    sgst = models.DecimalField(max_digits=5,decimal_places=2,editable=False)
    cgst = models.DecimalField(max_digits=5,decimal_places=2,editable=False)
    cess = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    
    def save(self,*args, **kwargs):
        if self.igst is not None:
            half_tax = self.igst/Decimal('2');
            self.cgst = half_tax;
            self.sgst = half_tax;
            
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.sac_code}"
    
class Category(models.Model):
    category = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return f"{self.category}"
    
class StockLocation(models.Model):
    store = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return f"{self.store}"

class ItemMaster(models.Model):
    supply_choices = [
        ("Goods","Goods"),
        ("Services","Services"),
    ]
    itemtype_choices = [
        ("FG","Finished Goods"),
        ("SFG","Semi-Finished Goods"),
        ("RM","Raw Materials"),
        ("CN","Consumables"),
        ("HW","Hardware"),
        ("OTH","Others"),
    ]
    name = models.CharField(max_length=200,unique=True)
    print_name = models.CharField(max_length=200,blank=True,null=True)
    item_type = models.CharField(max_length=20,choices=itemtype_choices)
    unit = models.ForeignKey(UOMMaster,on_delete=models.PROTECT)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    bom_required = models.BooleanField(default=False)
    hsncode = models.ForeignKey(HSNCode,on_delete=models.PROTECT,blank=True,null=True)
    saccode = models.ForeignKey(SACCode,on_delete=models.PROTECT,blank=True,null=True)
    supply_type = models.CharField(max_length=20,choices=supply_choices)
    is_active = models.BooleanField(default=True)
    
    def clean(self):
        if self.supply_type == "Goods":
            if not self.hsncode:
                raise ValidationError("Goods Must have an HSN code")
            if self.saccode:
                raise ValidationError("Goods can't have a SAC code")
            
        if self.supply_type == "Services":
            if not self.saccode:
                raise ValidationError("Services must have a SAC code")
            if self.hsncode:
                raise ValidationError("Services can't have a HSN code")
                
    
    def __str__(self):
        return f"{self.item_type} - {self.name}"