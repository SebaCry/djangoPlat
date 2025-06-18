from django.test import TestCase
from patients.models import Patient
from doctors.models import Doctor
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class DoctorViewSetTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='Sebastian',
            last_name='Perez',
            date_of_birth='2007-08-18',
            contact_number='3223151556',
            email='example@example.com',
            address='Calle 93 # 20 - 40 sur',
            medical_history='Ninguna',
        )

        self.doctor = Doctor.objects.create(
            first_name='Rodrigo',
            last_name='Riaño',
            qualification ='Profesional',
            contact_number='3102832409',
            email='example2@example.com', 
            address='Ibague',
            biography='Sin',
            is_on_vacation=False,
        )

        self.client = APIClient

    def test_list_should_return_200(self):
        url = reverse('doctor-appointments', kwargs={"pk" : self.doctor.id})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Create your tests here.
