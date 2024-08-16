import graphene

from supplier.models import Supplier
from supplier.types import SupplierType


class Query(graphene.ObjectType):
    suppliers = graphene.List(SupplierType, min_kwh_limit=graphene.Int())

    def resolve_suppliers(self, info, min_kwh_limit=None):
        if min_kwh_limit:
            return Supplier.objects.filter(minimum_kwh_limit__lte=min_kwh_limit)
        return Supplier.objects.all()
