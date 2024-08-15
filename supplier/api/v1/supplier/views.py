from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from supplier.api.v1.supplier.serializers import SupplierSerializer
from supplier.models import Supplier


class SupplierListV1(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,]
    serializer_class = SupplierSerializer
    filter_backends = [filters.OrderingFilter,
                       filters.SearchFilter,
                       DjangoFilterBackend]
    ordering_fields = ['name', 'created_at',
                       'cost_per_kwh', 'minimum_kwh_limit']
    search_fields = ['name']

    def get_queryset(self):
        return Supplier.objects.all().order_by('name')
