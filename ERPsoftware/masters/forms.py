from django import forms
from .models import HSNCode,ItemMaster,SACCode,Category,StockLocation,UOMMaster,State,AccountMaster

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
        
class SACForm(forms.ModelForm):
    class Meta:
        model = SACCode
        fields = ['sac_code','description','igst','cess']
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemMaster
        fields = ['name','print_name','item_type','unit','category','bom_required','hsncode','saccode','supply_type','is_active']
        
class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['state','state_code']
        
class AccountForm(forms.ModelForm):
    class Meta: 
        model = AccountMaster
        fields = ['ledger_name','GST_No','Address','contact_person','phone1','phone2','email','IT_Pan_No','Account_category','Bank_name','AC_No','IFSC_code','Branch_code','state','is_active']