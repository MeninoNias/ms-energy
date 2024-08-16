from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(f'v1/', include('supplier.api.v1.supplier.urls')),
]
