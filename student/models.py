# student/models.py
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10, choices=(("Present", "Present"), ("Absent", "Absent"))
    )

    def __str__(self):
        return f"{self.student.username} - {self.date} - {self.status}"
