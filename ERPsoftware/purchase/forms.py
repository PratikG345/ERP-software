from django import forms
from .models import PO_type
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PoTypeForm(forms.ModelForm):
    class Meta:
        model = PO_type
        fields = "__all__"
        
class UserRegistrationForm(UserCreationForm):
    dept = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username','email','dept','password1','password2')
