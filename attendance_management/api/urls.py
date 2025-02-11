from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, DepartmentViewSet, StudentViewSet, CourseViewSet, AttendanceLogViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'attendance', AttendanceLogViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
