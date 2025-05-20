from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Product

class ProductTemplateView(TemplateView):
    template_name = "productos/productos.html"

    def get_context_data(self):
        productos = Product.objects.all()

        return {
            "productos" : productos
        }


# Create your views here.
