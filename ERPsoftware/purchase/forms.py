from django import forms
from .models import PO_type,PurchaseOrder,PurchaseOrderLine
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PoTypeForm(forms.ModelForm):
    class Meta:
        model = PO_type
        fields = "__all__"
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['vendor','po_type','payment_terms','transport']
        
class PurchaseLine(forms.ModelForm):
    
    class Meta:
        model = PurchaseOrderLine
        fields = ['purchase_order','item','unit','qty','rate','igst_rate']
        
class UserRegistrationForm(UserCreationForm):
    dept = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username','email','dept','password1','password2')
