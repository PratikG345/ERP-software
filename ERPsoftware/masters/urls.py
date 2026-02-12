from django.urls import path
from .views import itemMaster,home,hsncode,saccode,stocklocation,category,uommaster,add_stck_loc,edit_stck_loc,delete_stck_loc
from .views import add_category,edit_category,delete_category
from .views import add_unit,edit_unit,delete_unit

urlpatterns = [
    path('',home,name="home"),
    path('itemMaster/',itemMaster,name="itemMaster"),
    path('hsncode/',hsncode,name="hsncode"),
    path('saccode/',saccode,name="saccode"),
    # -----------Stock Location----------------
    path('stocklocation/',stocklocation,name="stocklocation"),
    path('stocklocation/add_stock',add_stck_loc,name="add_stck_loc"),
    path('stocklocation/edit_stock/<int:store_id>',edit_stck_loc,name="edit_stck_loc"),
    path('stocklocation/delete_stock/<int:store_id>',delete_stck_loc,name="delete_stck_loc"),
    #-------------------------------------------
    
    # -----------Stock Location----------------
    path('category/',category,name="category"),
    path('category/add_category',add_category,name="add_category"),
    path('category/edit_category/<int:cat_id>',edit_category,name="edit_category"),
    path('category/delete_category/<int:cat_id>',delete_category,name="delete_category"),
    #-------------------------------------------
    
    # -----------UOMMaster----------------
    path('uommaster/',uommaster,name="uommaster"),
    path('uommaster/add_unit',add_unit,name="add_unit"),
    path('uommaster/edit_unit/<int:unit_id>',edit_unit,name="edit_unit"),
    path('uommaster/delete_unit/<int:unit_id>',delete_unit,name="delete_unit"),
    #-------------------------------------------
]