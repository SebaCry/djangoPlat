from . import views
from django.urls import path

urlpatterns = [
    path('mi-pedido/', views.MyOrderView.as_view(), name='mi_pedido'),
    path('agregar-producto/', views.CreateOrderProductView.as_view(), name='add_product')
]
