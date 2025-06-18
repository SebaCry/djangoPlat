from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from bookings.serializers import AppointmentSerializer
from bookings.models import Appointment
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import DoctorSerializer,DepartmentSerializer,DoctorAvailabilitySerializer,MedicalNoteSerializer
from .models import Doctor,Department,DoctorAvailability,MedicalNote

from .permissions import IsDoctor

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsDoctor]

    @action(['POST'], detail=True, url_path='set-on-vacation')
    def set_on_vacation(self, request, pk): 
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status" : "Doctor en vacaciones"})
    
    @action(['POST'], detail=True, url_path='set-off-vacation')
    def set_off_vacation(self, request, pk): 
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status" : "Doctor No esta en vacaciones"})
    
    @action(['POST', 'GET', 'DELETE'], detail=True, serializer_class=AppointmentSerializer)
    def appointments(self, request, pk):
        doctor = self.get_object()
        data = request.data.copy()
        data['doctor'] = doctor.id

        if request.method == 'POST':
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        if request.method == 'GET':
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        if request.method == 'DELETE' and pk:
            id = Appointment.objects.get(id=pk)
            try:
                serializer = self.serializer_class(id)
                id.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Appointment.DoesNotExist:
                return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
            


            


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

class MedicalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()