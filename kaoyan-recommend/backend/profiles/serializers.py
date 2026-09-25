from rest_framework import serializers
from .models import StudentProfile

class StudentProfileSerializer(serializers.ModelSerializer):
    rank_percent = serializers.RegexField(
        regex=r'^(前\d+%|\d+/\d+)$',
        error_messages={"invalid": "成绩排名格式应为'前X%'或'X/Y'"}
    )
    class Meta:
        model = StudentProfile
        fields = '__all__'