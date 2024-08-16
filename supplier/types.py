from graphene_django import DjangoObjectType

from supplier.models import Supplier


class SupplierType(DjangoObjectType):
    class Meta:
        model = Supplier
        fields = (
            'public_id', 'name', 'cnpj', 'logo', 'origin_state', 'cost_per_kwh',
            'minimum_kwh_limit', 'total_clients', 'average_rating'
        )
