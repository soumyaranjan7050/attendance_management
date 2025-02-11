from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return self.full_name

class Department(models.Model):
    department_name = models.CharField(max_length=255)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_class = models.CharField(max_length=100)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50)
    student_class = models.CharField(max_length=100)
    lecture_hours = models.IntegerField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

class AttendanceLog(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    present = models.BooleanField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Attendance: {self.student.full_name} - {self.course.course_name}"
