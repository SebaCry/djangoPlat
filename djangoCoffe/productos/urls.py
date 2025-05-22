from django.urls import path

from . import views

urlpatterns = [
    path('agregar/', views.ProductFormView.as_view(), name="add_product2"),
    path('api/', views.ProductListAPI.as_view(), name="productos_api"),
    path('', views.ProductListView.as_view(), name="productos")
]


