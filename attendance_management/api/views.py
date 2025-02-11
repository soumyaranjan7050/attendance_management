from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Department, Student, Course, AttendanceLog
from .serializers import UserSerializer, DepartmentSerializer, StudentSerializer, CourseSerializer, AttendanceLogSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class AttendanceLogViewSet(viewsets.ModelViewSet):
    queryset = AttendanceLog.objects.all()
    serializer_class = AttendanceLogSerializer
    permission_classes = [IsAuthenticated]

