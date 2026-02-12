from django.shortcuts import render,redirect,get_object_or_404
from .models import UOMMaster,State,HSNCode,SACCode,Category,StockLocation,ItemMaster
from .forms import StockLocForm, CatForm, UnitForm
# Create your views here.

def home(req):
    return render(req,'home.html')

def itemMaster(req):
    return render(req,'item_master.html')

def hsncode(req):
    return render(req,'hsncode.html')

def saccode(req):
    return render(req,'saccode.html')
# -------- Category View Start------------------
def category(req):
    category = Category.objects.all()
    return render(req,'category/category.html',{'category':category})

def add_category(req):
    if req.method == "POST":
        form = CatForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CatForm()
    return render(req,'category/categoryform.html',{'Catform':form})

def edit_category(req,cat_id):
    category = get_object_or_404(Category,pk=cat_id)
    if req.method == "POST":
        form = CatForm(req.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CatForm(instance = category)
    return render(req,'category/categoryform.html',{'Catform':form})
        
def delete_category(req,cat_id):
    category = get_object_or_404(Category,pk=cat_id)
    category.delete()
    return redirect('category')
# -------- Category View End------------------

# -------- Stock View Start------------------
def stocklocation(req):
    stock = StockLocation.objects.all()
    return render(req,'stock/stocklocation.html',{'stock':stock})

def add_stck_loc(req):
    if req.method == "POST":
        stockform = StockLocForm(req.POST)
        if stockform.is_valid():
            stockform.save()
            return redirect('stocklocation')
    else:
        stockform = StockLocForm()
    return render(req,'stock/stockform.html',{'stockform':stockform})

def edit_stck_loc(req,store_id):
    stock = get_object_or_404(StockLocation,pk=store_id)
    if req.method == "Post":
        stockform = StockLocForm(req.POST,instance=stock)
        if stockform.is_valid():
            stockform.save()
            return redirect('stocklocation')
    else:
        stockform = StockLocForm(instance=stock)
    return render(req,'stock/stockform.html',{'stockform':stockform})

def delete_stck_loc(req,store_id):
    stock = get_object_or_404(StockLocation,pk=store_id)
    stock.delete()
    return redirect('stocklocation')
# -------- Stock View End------------------+

# -------- UOM View Start------------------
def uommaster(req):
    uom = UOMMaster.objects.all()
    return render(req,'uommaster.html',{'uom':uom})

def create_unit(req):
    if req.method == "POST":
        unitform = UnitForm(req.POST)
        if unitform.is_valid():
            unitform.save()
            return redirect('uommaster')
    else:
        unitform = UnitForm()
    return render(req,'unitform.html',{'unitform':unitform})

def edit_unit(req,unit_id):
    unit = get_object_or_404(UOMMaster,pk=unit_id)
    if req.method == "POST":
        unitform = get_object_or_404(UOMMaster,instance = unit)
        if unitform.is_valid():
            unitform.save()
            return redirect('uommaster')
    else:
        unitform = UnitForm()
    return render(req,'unitform.html',{'unitform':unitform})

def delete_unit(req,unit_id):
    unit = get_object_or_404(UOMMaster,pk=unit_id)
    unit.delete()
    return redirect('uommaster')
# -------- UOM View End------------------
