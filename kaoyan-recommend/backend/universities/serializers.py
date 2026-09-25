from rest_framework import serializers
from .models import University, Major, Admission

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = '__all__'

class MajorSerializer(serializers.ModelSerializer):
    admissions = AdmissionSerializer(many=True, read_only=True)
    class Meta:
        model = Major
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):
    majors = MajorSerializer(many=True, read_only=True)
    class Meta:
        model = University
        fields = '__all__'