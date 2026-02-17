from django.urls import path
from .views import itemMaster,home,hsncode,saccode,stocklocation,category,uommaster,add_stck_loc,edit_stck_loc,delete_stck_loc,state,account
from .views import add_category,edit_category,delete_category
from .views import add_unit,edit_unit,delete_unit
from .views import add_hsn,edit_hsn,delete_hsn
from .views import add_sac,edit_sac,delete_sac
from .views import add_item,edit_item,delete_item
from .views import add_state,edit_state,delete_state
from .views import add_account,edit_account,delete_account

urlpatterns = [
    path('',home,name="home"),
    #-----------Item Master----------------------
    path('itemMaster/',itemMaster,name="itemMaster"),
    path('itemMaster/add_item',add_item,name="add_item"),
    path('itemMaster/edit_item/<int:item_id>',edit_item,name="edit_item"),
    path('itemMaster/delete_item/<int:item_id>',delete_item,name="delete_item"),
    #-------------------------------------------
    
    #-----------Account----------------------
    path('account/add_account',add_account,name="add_account"),
    path('account/',account,name="account"),
    path('account/edit_account/<int:account_id>',edit_account,name="edit_account"),
    path('account/delete_account/<int:account_id>',delete_account,name="delete_account"),
    #-------------------------------------------
    
    #-----------State----------------------
    path('state/add_state',add_state,name="add_state"),
    path('state/',state,name="state"),
    path('state/edit_state/<int:state_id>',edit_state,name="edit_state"),
    path('state/delete_state/<int:state_id>',delete_state,name="delete_state"),
    #-------------------------------------------
    
    #-----------HSN Code----------------------
    path('HSNCode/',hsncode,name="hsncode"),
    path('HSNCode/add_hsn',add_hsn,name="add_hsn"),
    path('HSNCode/edit_hsn/<int:hsn_id>',edit_hsn,name="edit_hsn"),
    path('HSNCode/delete_hsn/<int:hsn_id>',delete_hsn,name="delete_hsn"),
    #-------------------------------------------
    
    #-----------SAC Code----------------------
    path('SACCode/add_sac',add_sac,name="add_sac"),
    path('SACCode/',saccode,name="saccode"),
    path('SACCode/edit_sac/<int:sac_id>',edit_sac,name="edit_sac"),
    path('SACCode/delete_sac/<int:sac_id>',delete_sac,name="delete_sac"),
    #-------------------------------------------
    
    # -----------Stock Location----------------
    path('stocklocation/',stocklocation,name="stocklocation"),
    path('stocklocation/add_stock',add_stck_loc,name="add_stck_loc"),
    path('stocklocation/edit_stock/<int:store_id>',edit_stck_loc,name="edit_stck_loc"),
    path('stocklocation/delete_stock/<int:store_id>',delete_stck_loc,name="delete_stck_loc"),
    #-------------------------------------------
    
    # -----------Category----------------
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