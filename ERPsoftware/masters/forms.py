from django import forms
from .models import HSNCode,ItemMaster,SACCode,Category,StockLocation,UOMMaster

class StockLocForm(forms.ModelForm):
    class Meta:
        model = StockLocation;
        fields = ['store']
        
class CatForm(forms.ModelForm):
    class Meta:
        model = Category;
        fields = ['category']

class UnitForm(forms.ModelForm):
    class Meta:
        model = UOMMaster;
        fields = ['unit','fullform']
        
class HSNForm(forms.ModelForm):
    class Meta:
        model = HSNCode
        fields = ['hsn_code','description','igst','cess']