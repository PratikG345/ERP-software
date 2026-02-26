from django import forms
from .models import PO_type,PurchaseOrder,PurchaseOrderLine
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

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
        fields = ['item','unit','qty','rate']
        widgets = {
            'item':forms.Select(attrs={'class':'item'}),
            'unit':forms.Select(attrs={'class':'unit bg-danger','readonly':'readonly'}),
            'qty':forms.NumberInput(attrs={'class':'qty border-0 bg-dark'}),
            'rate':forms.NumberInput(attrs={'class':'rate border-0 bg-dark'}),
        }
        
class UserRegistrationForm(UserCreationForm):
    dept = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username','email','dept','password1','password2')
        
PurchaseLineFormSet = inlineformset_factory(
    PurchaseOrder,
    PurchaseOrderLine,
    form=PurchaseLine,
    extra=1,
    can_delete=True
)
