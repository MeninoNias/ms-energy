from django.urls import path, include

from .views import SupplierListV1

urlpatterns = [
    path(f'fornecedores', SupplierListV1.as_view(), name='supplier_list'),
]
