from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import Product
from .forms import ProductForm

class ProductFormView(generic.FormView):
    template_name = "productos/add_producto.html"
    form_class = ProductForm
    success_url = reverse_lazy('productos')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductListView(generic.ListView):
    model = Product
    template_name = "productos/productos.html"
    context_object_name = 'productos'




# Create your views here.
