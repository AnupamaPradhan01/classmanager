from django.db import models


class Attendance(models.Model):
    ATTENDANCE_CHOICES = [
        ("Present", "Present"),
        ("Late", "Late"),
        ("Absent", "Absent"),
        ("Holiday", "Holiday"),
        ("Halfday", "Halfday"),
    ]

    student = models.ForeignKey("student.Student", on_delete=models.CASCADE)
    teacher = models.ForeignKey("teacher.Teacher", on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.status} on {self.date}"


class Teacher_Attendance(models.Model):
    ATTENDANCE_CHOICES = [
        ("Present", "Present"),
        ("Absent", "Absent"),
        ("Holiday", "Holiday"),
        ("Halfday", "Halfday"),
    ]
    teacher = models.ForeignKey("teacher.Teacher", on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)

    def __str__(self):
        return f"{self.teacher.first_name} {self.teacher.last_name} - {self.status} on {self.date}"
