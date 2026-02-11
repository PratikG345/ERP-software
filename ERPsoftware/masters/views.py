from django.shortcuts import render
from .models import UOMMaster,State,HSNCode,SACCode,Category,StockLocation,ItemMaster
# Create your views here.

def home(req):
    return render(req,'home.html')

def itemMaster(req):
    return render(req,'item_master.html')

def hsncode(req):
    return render(req,'hsncode.html')

def saccode(req):
    return render(req,'saccode.html')

def category(req):
    return render(req,'category.html')

def stocklocation(req):
    return render(req,'stocklocation.html')

def uommaster(req):
    return render(req,'uommaster.html')

