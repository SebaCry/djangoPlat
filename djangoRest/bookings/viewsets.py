from rest_framework import viewsets
from .serializers import MedicalNoteSerializer, AppointmentSerializer
from .models import MedicalNote, Appointment

class MedicalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()