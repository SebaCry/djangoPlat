from rest_framework import serializers
from .models import Doctor, DoctorAvailability, MedicalNote, Department

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_email(self, value):
        if "@example.com" in value:
            return value
        
        raise serializers.ValidationError("El correo debe incluir @example.com")
    
    def validate(self, attrs):
        attrs['email']
        if len(attrs['contact_number']) < 10 and attrs['is_on_vacation'] == True:
            raise serializers.ValidationError("Por favor ingresa un numero valido antes de ir a vacaciones")


        return super().validate(attrs)


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = '__all__' 


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__' 

        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__' 