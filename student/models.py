# student/models.py
from accounts.models import CustomUser
from django.db import models


class StudentProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="student_profile"
    )
    roll_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    class_name = models.CharField(max_length=50)  # e.g., "10th Grade", "12th Science"
    section = models.CharField(
        max_length=10, null=True, blank=True
    )  # e.g., "A", "B", etc.
    student_phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    parent_name = models.CharField(max_length=100, null=True, blank=True)
    parent_phone_number = models.CharField(max_length=15, null=True, blank=True)
    admission_date = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to="student_photos/", null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username} ({self.class_name} - {self.section})"
