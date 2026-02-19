from django.shortcuts import render

# Create your views

def po_type(request):
    return render(request,'purchase/po_type.html')