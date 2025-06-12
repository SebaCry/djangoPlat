from django.db import models

from doctors.models import Doctor
from patients.models import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField()
    status = models.CharField(max_length=10)

class MedicalNote(models.Model):
    appointment = models.ForeignKey(
        Appointment, related_name='medical_notes', on_delete=models.CASCADE
    )
    note = models.TextField()
    date = models.DateField()

# Create your models here.
