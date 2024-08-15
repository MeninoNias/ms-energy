from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(f'supplier/', include('supplier.api.v1.urls')),
]
