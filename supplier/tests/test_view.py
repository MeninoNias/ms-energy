from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from supplier.models import Supplier


class SupplierListV1TestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = RefreshToken.for_user(self.user).access_token

        # Cria fornecedores para testar a filtragem
        Supplier.objects.create(
            name="Fornecedor 1",
            cnpj="00000000000100",
            origin_state="SP",
            cost_per_kwh=0.50,
            minimum_kwh_limit=10000,
            total_clients=200,
            average_rating=4.5,
        )
        Supplier.objects.create(
            name="Fornecedor 2",
            cnpj="00000000000200",
            origin_state="RJ",
            cost_per_kwh=0.70,
            minimum_kwh_limit=5000,
            total_clients=150,
            average_rating=3.8,
        )

    def test_supplier_list_authenticated(self):
        url = reverse('supplier_list')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_supplier_list_unauthenticated(self):
        url = reverse('supplier_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_supplier_list_filter_min_kwh_limit(self):
        url = reverse('supplier_list') + '?min_kwh_limit=10000'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['name'], 'Fornecedor 1')

    def test_supplier_list_ordering(self):
        url = reverse('supplier_list') + '?ordering=cost_per_kwh'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'Fornecedor 1')
        self.assertEqual(response.data['results'][1]['name'], 'Fornecedor 2')

    def test_supplier_list_search(self):
        url = reverse('supplier_list') + '?search=Fornecedor 1'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'Fornecedor 1')
