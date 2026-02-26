from django.urls import path                                                
from .views import po_type,add_po_type,delete_po_type,edit_po_type
from .views import po,add_po,edit_po,delete_po

urlpatterns = [
    path('po_type/',po_type,name='po_type'),
    path('add_po_type/',add_po_type,name='add_po_type'),
    path('edit_po_type/<potype_id>',edit_po_type,name='edit_po_type'),
    path('delete_po_type/<potype_id>',delete_po_type,name='delete_po_type'),
    
    path('po/',po,name='po'),
    path('add_po/',add_po,name='add_po'),
    path('edit_po/<potype_id>',edit_po,name='edit_po'),
    path('delete_po/<potype_id>',delete_po,name='delete_po'),
]
