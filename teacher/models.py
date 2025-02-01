# student/models.py
from accounts.models import CustomUser
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


class Attendance(models.Model):
    student = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="attendance_records"
    )
    class_name = models.CharField(max_length=50)  # Specify class like "10-A"
    date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=[("Present", "Present"), ("Absent", "Absent")]
    )
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="marked_attendance"
    )

    def __str__(self):
        return (
            f"{self.class_name} - {self.student.username} - {self.date} - {self.status}"
        )


class Assignment(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assignments"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} ({self.class_name})"


class Submission(models.Model):
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name="submissions"
    )
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="submissions"
    )
    submission_file = models.FileField(upload_to="assignments/submissions/")
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=10, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.assignment.title} - {self.student.username}"
