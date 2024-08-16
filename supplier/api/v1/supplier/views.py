import django_filters
from django_filters import NumberFilter
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from supplier.api.v1.supplier.serializers import SupplierSerializer
from supplier.models import Supplier


class SupplierFilter(django_filters.FilterSet):
    min_kwh_limit = NumberFilter(field_name='minimum_kwh_limit', lookup_expr='lte')

    class Meta:
        model = Supplier
        fields = ['min_kwh_limit', 'public_id', 'origin_state', 'average_rating', 'total_clients']


class SupplierListV1(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = SupplierSerializer
    filter_backends = [filters.OrderingFilter,
                       filters.SearchFilter,
                       DjangoFilterBackend]
    filterset_class = SupplierFilter
    ordering_fields = ['name', 'created_at', 'cost_per_kwh', 'minimum_kwh_limit']
    search_fields = ['name']

    def get_queryset(self):
        """
            This view should return a list of all the Supplier.
        """
        return Supplier.objects.all().order_by('name')
