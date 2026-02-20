from django.shortcuts import render,redirect,get_object_or_404
from .models import PO_type
from .forms import PoTypeForm
# Create your views

def po_type(req):
    po = PO_type.objects.all()
    return render(req,'purchase/po_type.html',{'po':po})

def add_po_type(req):
    if req.method == "POST":
        po_type_form = PoTypeForm(req.POST)
        if po_type_form.is_valid():
            po_type_form.save()
            return redirect('po_type')
    else:
        po_type_form = PoTypeForm()
        return render(req,'purchase/po_type_form.html',{'po_type_form':po_type_form})
    
def edit_po_type(req,potype_id):
    po_type = get_object_or_404(PO_type,pk=potype_id)
    if req.method == "POST":
        po_type_form = PoTypeForm(req.POST,instance=po_type)
        if po_type_form.is_valid():
            po_type_form.save()
            return redirect('po_type')
    else:
        po_type_form = PoTypeForm(instance=po_type)
        return render(req,'purchase/po_type_form.html',{'po_type_form':po_type_form})
    
def delete_po_type(req,potype_id):
    po_type = get_object_or_404(PO_type,pk=potype_id)
    po_type.delete()
    return redirect('po_type')
    