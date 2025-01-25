# student/models.py
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student_profile"
    )
    class_name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=20, unique=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True
    )
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10, choices=(("Present", "Present"), ("Absent", "Absent"))
    )

    def __str__(self):
        return f"{self.student.username} - {self.date} - {self.status}"
