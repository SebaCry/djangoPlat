from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from .serializers import ProductSerializer
from .models import Product
from .forms import ProductForm
from rest_framework.views import APIView
from rest_framework.response import Response
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

class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        productos = Product.objects.all()
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data)

# Create your views here.
