from .serializers import MedicalNoteSerializer, AppointmentSerializer
from .models import MedicalNote, Appointment
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
)

class MedicalNoteView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = AppointmentSerializer
    queryset = MedicalNote.objects.all()

class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

class AppointmentView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class DetailAppointmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

# Create your views here.
