from django.db import models

# Create your models here.
class UOMmaster(models.Model):
    unit = models.CharField(max_length=10,null=True,blank=True)
    fullform = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f"{self.unit}-{self.fullform}"
    
class State(models.Model):
    state = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return f"{self.state}"
    
class HSNcode(models.Model):
    hsn_code = models.CharField(max_length=8,unique=True)
    description = models.TextField(blank=True,null=True)
    igst = models.DecimalField(max_digits=5,decimal_places=2)
    sgst = models.DecimalField(max_digits=5,decimal_places=2,editable=False)
    cgst = models.DecimalField(max_digits=5,decimal_places=2,editable=False)
    cess = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    
    def save(self,*args, **kwargs):
        if self.igst is not None:
            half_tax = self.igst/2;
            self.cgst = half_tax;
            self.sgst = half_tax;
            
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.hsn_code}"
    
class ItemType(models.Model):
    item_code = models.CharField(max_length=2,unique=True)
    category = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return f"{self.item_code} - {self.category}"