from rest_framework import serializers
from .models import User, Department, Student, Course, AttendanceLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name', 'type']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class AttendanceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceLog
        fields = '__all__'
