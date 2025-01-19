# student/models.py
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Timetable(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_timetables"
    )  # Link timetable to teacher
    day = models.CharField(
        max_length=10,
        choices=[
            ("Monday", "Monday"),
            ("Tuesday", "Tuesday"),
            ("Wednesday", "Wednesday"),
            ("Thursday", "Thursday"),
            ("Friday", "Friday"),
            ("Saturday", "Saturday"),
            ("Sunday", "Sunday"),
        ],
    )
    subject = models.CharField(max_length=100)
    time = models.TimeField()
    class_name = models.CharField(max_length=50)  # Specify class (e.g., "Class 10-A")

    def __str__(self):
        return f"{self.class_name} - {self.day} - {self.subject} - {self.time}"
