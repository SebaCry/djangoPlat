from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductTemplateView.as_view())
]
