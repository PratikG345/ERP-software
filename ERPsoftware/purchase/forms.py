from django.forms import forms
from .models import PO_type

class PoTypeForm(forms.ModelForm):
    class Meta:
        model = PO_type
        fields = "__all__"