from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from .forms import OrderProductForm
from .models import Order, OrderProduct
from django.contrib.auth.mixins import LoginRequiredMixin

class MyOrderView(LoginRequiredMixin ,DetailView):
    model = Order
    template_name = 'orders/my_order.html'
    context_object_name = 'order'

    def get_object(self, queryset = None):
        return Order.objects.filter(is_Active=True, user=self.request.user).first()


# Create your views here.
class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = 'orders/create_order_product.html'
    form_class = OrderProductForm
    success_url = reverse_lazy('mi_pedido')

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(is_Active=True, user=self.request.user)
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)