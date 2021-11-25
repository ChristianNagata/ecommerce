from rest_framework.test import APITestCase
from products.models import Product
from django.urls import reverse


class ProductTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Products-list')
