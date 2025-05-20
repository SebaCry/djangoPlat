from django.urls import path

from . import views

urlpatterns = [
    path('agregar/', views.ProductFormView.as_view(), name="add_product"),
    path('', views.ProductListView.as_view(), name="productos")
]


