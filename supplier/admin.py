from django.contrib import admin

from supplier.models import Supplier


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_filter = ('origin_state',)
    list_display = ('name', 'origin_state', 'minimum_kwh_limit',)
