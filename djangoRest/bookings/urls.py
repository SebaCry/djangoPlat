from .views import ( 
    MedicalNoteView,
    DetailMedicalNoteView,
    AppointmentView,
    DetailAppointmentView
)
from django.urls import path
from .viewsets import MedicalNoteViewSet, AppointmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('appoinments', AppointmentViewSet)
router.register('medical-note', MedicalNoteViewSet)



urlpatterns = [
    
] + router.urls
