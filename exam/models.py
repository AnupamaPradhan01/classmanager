from django.db import models


class Exam(models.Model):
    EXAM_CHOICES = [
        ("Week Test", "Week Test"),
        ("Monthly Test", "Monthly Test"),
        ("Unit Test", "Unit Test"),
        ("Progress Test ", "Progress Test"),
        ("Oral Test", "Oral Test"),
        ("Quaterly Exam", "Quaterly Exam"),
        ("Half-Yearly Exam", "Half-Yearly Exam"),
        ("Annual Exam", "Annual Exam"),
    ]

    TIME_CHOICES = [
        ("08:00 AM", "08:00 AM"),
        ("10:00 AM", "10:00 AM"),
        ("12:00 PM", "12:00 PM"),
        ("02:00 PM", "02:00 PM"),
        ("04:00 PM", "04:00 PM"),
    ]

    exam_name = models.CharField(max_length=50, choices=EXAM_CHOICES)
    exam_date = models.DateField()
    start_time = models.CharField(max_length=10, choices=TIME_CHOICES)
    end_time = models.CharField(max_length=10, choices=TIME_CHOICES)

    def __str__(self):
        return f"{self.exam_name} - {self.exam_date}"
