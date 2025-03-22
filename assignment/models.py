from django.db import models
from teacher.models import CLASS_CHOICES, SECTION_CHOICES


# Create your models here.
class TeacherAssignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to="assignments/teacher/", blank=True, null=True)
    class_nu = models.CharField(max_length=100, choices=CLASS_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    teacher = models.ForeignKey("teacher.Teacher", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class StudentAssignmentUpload(models.Model):
    assignment = models.ForeignKey("TeacherAssignment", on_delete=models.CASCADE)
    student = models.ForeignKey("student.Student", on_delete=models.CASCADE)
    file = models.FileField(upload_to="assignments/teacher/", blank=True, null=True)
    uploaded_time = models.DateTimeField(auto_now_add=True)
