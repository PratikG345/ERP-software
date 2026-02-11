from django.urls import path
from .views import itemMaster,home,hsncode,saccode,stocklocation,category,uommaster

urlpatterns = [
    path('',home,name="home"),
    path('itemMaster/',itemMaster,name="itemMaster"),
    path('hsncode/',hsncode,name="hsncode"),
    path('saccode/',saccode,name="saccode"),
    path('stocklocation/',stocklocation,name="stocklocation"),
    path('category/',category,name="category"),
    path('uommaster/',uommaster,name="uommaster"),
]