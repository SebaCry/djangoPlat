from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ListPatientsView, DetailPatientsView
from .viewsets import InsuranceViewSet, PatientViewSet, MedicalRecordViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('medical-record', MedicalRecordViewSet)
router.register('insurance', InsuranceViewSet)

urlpatterns = [

] + router.urls
