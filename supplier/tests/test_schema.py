from graphene_django.utils.testing import GraphQLTestCase

from core.schema import schema
from supplier.models import Supplier


class SupplierQueryTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def setUp(self):
        Supplier.objects.create(
            name="Fornecedor 1",
            cnpj="00000000000100",
            origin_state="SP",
            cost_per_kwh=0.50,
            minimum_kwh_limit=10000,
            total_clients=200,
            average_rating=4.5,
        )

    def test_suppliers_query(self):
        response = self.query(
            '''
            query {
                suppliers(minKwhLimit: 10000) {
                    publicId
                    name
                    cnpj
                    logo
                    originState
                    costPerKwh
                    minimumKwhLimit
                    totalClients
                    averageRating
                }
            }
            ''',
        )
        content = response.json()
        self.assertResponseNoErrors(response)
        self.assertEqual(len(content['data']['suppliers']), 1)
        self.assertEqual(content['data']['suppliers'][0]['name'], 'Fornecedor 1')
        self.assertEqual(content['data']['suppliers'][0]['originState'], 'SP')
