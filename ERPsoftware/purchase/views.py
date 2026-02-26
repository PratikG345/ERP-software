from django.shortcuts import render,redirect,get_object_or_404
from .models import PO_type,PurchaseOrder,PurchaseOrderLine
from .forms import PoTypeForm,PurchaseForm,PurchaseLineFormSet
from masters.models import ItemMaster
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

def po(req):
    po = PurchaseOrder.objects.all()
    context = {
        'po':po,
    }
    return render(req,'purchase/purchase_order.html',context)


def add_po(req):
    if req.method == "POST":
        form = PurchaseForm(req.POST)
        formset = PurchaseLineFormSet(req.POST)
        
        if form.is_valid() and formset.is_valid():
            po=form.save()
            formset.instance=po
            formset.save()
            return redirect('po')
    else:
        form = PurchaseForm()
        formset = PurchaseLineFormSet()
    context = {
        'form':form,
        'formset':formset,
        'items_units': {item.id: item.unit.id for item in ItemMaster.objects.all()}
    }
    return render(req,'purchase/purchase_form.html',context)

def edit_po(req, po_id):
    po = get_object_or_404(PurchaseOrder, pk=po_id)

    if req.method == "POST":
        form = PurchaseForm(req.POST, instance=po)
        formset = PurchaseLineFormSet(req.POST, instance=po)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('po')
        else:
            print(form.errors)
            print(formset.errors)

    else:
        form = PurchaseForm(instance=po)
        formset = PurchaseLineFormSet(instance=po)

    return render(req, 'purchase/purchase_form.html', {
        'form': form,
        'formset': formset,
        'items_units': {item.id: item.unit.id for item in ItemMaster.objects.all()}
    })

def delete_po(req,po_id):
    po = get_object_or_404(PurchaseOrder,pk=po_id)
    po.delete()
    return redirect('po')