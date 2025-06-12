from django.urls import path
from .views import (
    ListDoctorView,
    DetailDoctorView,
    ListDepartmentView,
    DetailDepartmentView,
    ListDoctorAvailabilityView,
    DetailDoctorAvailabilityView,
    ListMedicalNoteView,
    DetailMedicalNoteView,
)
from .viewsets import DoctorViewSet, DepartmentViewSet, MedicalNoteViewSet, DoctorAvailabilityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('department', DepartmentViewSet)
router.register('medical-note', MedicalNoteViewSet)
router.register('doctor-availability', DoctorAvailabilityViewSet)


urlpatterns = [
    
] + router.urls
