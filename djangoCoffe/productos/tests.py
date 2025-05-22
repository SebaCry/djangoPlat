from django.test import TestCase
from django.urls import reverse_lazy

from .models import Product


class ProductListViewTest(TestCase):
    def test_should_return_200(self):
        url = reverse_lazy('productos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['productos'].count(), 0)

    def test_should_return_200_with_products(self):
        url = reverse_lazy('productos')
        Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.0,
            available=True,
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['productos'].count(), 1)

# Create your tests here.
