from django.contrib import admin
from .models import UOMMaster,State,HSNCode,SACCode,Category,StockLocation,ItemMaster
# Register your models here.
admin.site.register(UOMMaster)
admin.site.register(State)
admin.site.register(HSNCode)
admin.site.register(SACCode)
admin.site.register(Category)
admin.site.register(StockLocation)
admin.site.register(ItemMaster)
