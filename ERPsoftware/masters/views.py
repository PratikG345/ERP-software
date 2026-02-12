from django.shortcuts import render,redirect,get_object_or_404
from .models import UOMMaster,State,HSNCode,SACCode,Category,StockLocation,ItemMaster
from .forms import StockLocForm, CatForm, UnitForm, HSNForm, SACForm, ItemForm
# Create your views here.

def home(req):
    return render(req,'home.html')

# -------- Item Master Start------------------
def itemMaster(req):
    item = ItemMaster.objects.all()
    return render(req,'item/item_master.html',{'item':item})

def add_item(req):
    if req.method == "POST":
        itemform = ItemForm(req.POST)
        if itemform.is_valid():
            itemform.save()
            return redirect('itemMaster')
    else:
        itemform = ItemForm()
    return render(req,'item/itemform.html',{'itemform':itemform})

def edit_item(req,item_id):
    item = get_object_or_404(ItemMaster,pk = item_id)
    if req.method == "POST":
        itemform = ItemForm(req.POST,instance=item)
        if itemform.is_valid():
            itemform.save()
            return redirect('itemMaster')
    else:
        itemform = ItemForm(instance=item)
    return render(req,'item/itemform.html',{'itemform':itemform})

def delete_item(req,item_id):
    item = get_object_or_404(ItemMaster,pk=item_id)
    item.delete()
    return redirect('itemMaster')
# -------- Item Master End------------------

# -------- HSN View Start------------------
def hsncode(req):
    hsn = HSNCode.objects.all()
    return render(req,'hsn/hsncode.html',{'hsn':hsn})

def add_hsn(req):
    if req.method == "POST":
        hsnform = HSNForm(req.POST)
        if hsnform.is_valid():
            hsnform.save()
            return redirect('hsncode')
    else:
        hsnform = HSNForm()
    return render(req,'hsn/hsnform.html',{'hsnform':hsnform})

def edit_hsn(req,hsn_id):
    hsn = get_object_or_404(HSNCode,pk=hsn_id)
    if req.method == "POST":
        hsnform = HSNForm(req.POST,instance=hsn)
        if hsnform.is_valid():
            hsnform.save()
            return redirect('hsncode')
    else:
        hsnform = HSNForm(instance=hsn)
    return render(req,'hsn/hsnform.html',{'hsnform':hsnform})

def delete_hsn(req,hsn_id):
    hsn = get_object_or_404(HSNCode,pk=hsn_id)
    hsn.delete()
    return redirect('hsncode')
# -------- HSN View End------------------

# -------- SAC View Start------------------
def saccode(req):
    sac = SACCode.objects.all()
    return render(req,'sac/saccode.html',{'sac':sac})

def add_sac(req):
    if req.method == "POST":
        sacform = SACForm(req.POST)
        if sacform.is_valid():
            sacform.save()
            return redirect('saccode')
    else:
        sacform = SACForm()
    return render(req,'sac/sacform.html',{'sacform':sacform})

def edit_sac(req,sac_id):
    sac = get_object_or_404(SACCode,pk=sac_id)
    if req.method == "POST":
        sacform = SACForm(req.POST,instance=sac)
    else:
        sacform = SACForm(instance=sac)
    return render(req,'sac/sacform.html',{'sacform':sacform})

def delete_sac(req,sac_id):
    sac = get_object_or_404(SACCode,pk=sac_id)
    sac.delete()
    return redirect('saccode')
# -------- SAC View End------------------

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
    return render(req,'UOM/uommaster.html',{'uom':uom})

def add_unit(req):
    if req.method == "POST":
        unitform = UnitForm(req.POST)
        if unitform.is_valid():
            unitform.save()
            return redirect('uommaster')
    else:
        unitform = UnitForm()
    return render(req,'UOM/unitform.html',{'unitform':unitform})

def edit_unit(req,unit_id):
    units = get_object_or_404(UOMMaster,pk=unit_id)
    if req.method == "POST":
        unitform = UnitForm(req.POST,instance = units)
        if unitform.is_valid():
            unitform.save()
            return redirect('uommaster')
    else:
        unitform = UnitForm(instance=units)
    return render(req,'UOM/unitform.html',{'unitform':unitform})

def delete_unit(req,unit_id):
    unit = get_object_or_404(UOMMaster,pk=unit_id)
    unit.delete()
    return redirect('uommaster')
# -------- UOM View End------------------
