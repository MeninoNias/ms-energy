import graphene
from graphene_django import DjangoObjectType
from django.conf import settings
from supplier.models import Supplier


class SupplierType(DjangoObjectType):
    logo_url = graphene.String()
    
    class Meta:
        model = Supplier
        fields = (
            'public_id', 'name', 'cnpj', 'logo', 'origin_state', 'cost_per_kwh',
            'minimum_kwh_limit', 'total_clients', 'average_rating', 'logo_url'
        )

    def resolve_logo(self, info):
        if self.logo:
            return settings.APP_URL + settings.MEDIA_URL + str(self.logo)
        return 'https://placehold.co/100x100'
