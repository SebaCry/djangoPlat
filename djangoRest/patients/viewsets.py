from rest_framework import viewsets
from .serializers import PatientSerializer, MedicalRecordSerializer, InsuranceSerializer
from .models import Patient, MedicalRecord, Insurance
from rest_framework.decorators import action
from rest_framework.response import Response

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    @action(['GET'], detail=True)
    def get_medical_history(self, request, pk):
        patient = self.get_object()
        patient.medical_history
        return Response({'medical_history' : patient.medical_history})



class MedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()

class InsuranceViewSet(viewsets.ModelViewSet):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()