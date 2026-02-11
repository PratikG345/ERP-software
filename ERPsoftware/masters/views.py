from django.shortcuts import render,redirect,get_object_or_404
from .models import UOMMaster,State,HSNCode,SACCode,Category,StockLocation,ItemMaster
from .forms import StockLocForm, CatForm
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
    category = Category.objects.all()
    return render(req,'category.html',{'category':category})

def add_category(req):
    if req.method == "POST":
        form = CatForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CatForm()
    return render(req,'categoryform.html',{'form':form})

def edit_category(req,cat_id):
    category = get_object_or_404(Category,pk=cat_id)
    if req.method == "POST":
        form = CatForm(req.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CatForm(instance = category)
    return render(req,'categoryform.html',{'form':form})
        
def delete_category(req,cat_id):
    category = get_object_or_404(Category,pk=cat_id)
    category.delete()
    return redirect('category')

# -------------------------------------
def stocklocation(req):
    stock = StockLocation.objects.all()
    return render(req,'stocklocation.html',{'stock':stock})

def add_stck_loc(req):
    if req.method == "POST":
        stockform = StockLocForm(req.POST)
        if stockform.is_valid():
            stockform.save()
            return redirect('stocklocation')
    else:
        stockform = StockLocForm()
    return render(req,'stockform.html',{'stockform':stockform})

def edit_stck_loc(req,store_id):
    stock = get_object_or_404(StockLocation,pk=store_id)
    if req.method == "Post":
        stockform = StockLocForm(req.POST,instance=stock)
        if stockform.is_valid():
            stockform.save()
            return redirect('stocklocation')
    else:
        stockform = StockLocForm(instance=stock)
    return render(req,'stockform.html',{'stockform':stockform})

def delete_stck_loc(req,store_id):
    stock = get_object_or_404(StockLocation,pk=store_id)
    stock.delete()
    return redirect('stocklocation')

# --------------------------------------
def uommaster(req):
    return render(req,'uommaster.html')

