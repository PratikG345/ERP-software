from django.shortcuts import render
from .models import PO_type
# Create your views

def po_type(request):
    po = PO_type.objects.all()
    return render(request,'purchase/po_type.html',{'po':po})