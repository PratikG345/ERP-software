from django.urls import path                                                
from .views import po_type

urlpatterns = [
    path('po_type/',po_type,name='po_type'),
]
