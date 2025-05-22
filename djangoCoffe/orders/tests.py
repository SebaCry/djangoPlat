from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

class MyOrderViewTest(TestCase):
    def test_redirect_not_login(self):
        url = reverse_lazy('mi_pedido')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/usuarios/login/?next=/pedidos/mi-pedido/')

    def test_redirect_login(self):
        url = reverse_lazy('mi_pedido')
        user = get_user_model().objects.create(
            username='testuser'
        )
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


# Create your tests here.
