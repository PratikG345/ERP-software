from django.urls import path                                                
from .views import po_type,add_po_type,delete_po_type,edit_po_type

urlpatterns = [
    path('po_type/',po_type,name='po_type'),
    path('add_po_type/',add_po_type,name='add_po_type'),
    path('edit_po_type/<potype_id>',edit_po_type,name='edit_po_type'),
    path('delete_po_type/<potype_id>',delete_po_type,name='delete_po_type'),
]
