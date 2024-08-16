from django.test import TestCase
from django.urls import reverse

from supplier.models import Supplier


class GraphQlIntegrateTestCase(TestCase):

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

    def test_graphql_response_is_json(self):
        response = self.client.post(reverse('graphql'), data={
            'query': '{ suppliers { name } }'
        }, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertIsInstance(response.json(), dict)
