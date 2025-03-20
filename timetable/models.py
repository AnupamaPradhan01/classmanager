from django.core.validators import FileExtensionValidator
from django.db import models
from teacher.models import CLASS_CHOICES, SECTION_CHOICES


def timetable_upload_path(instance, filename):
    """Stores uploaded files in 'media/timetable/'"""
    return f"timetable/{filename}"


class Timetable(models.Model):
    class_no = models.CharField(max_length=100, choices=CLASS_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    timetable_file = models.FileField(
        upload_to=timetable_upload_path,  # Store in 'media/timetable/'
        validators=[
            FileExtensionValidator(allowed_extensions=["xls", "xlsx"])
        ],  # Restrict to Excel files
    )

    def __str__(self):
        return f"Timetable for Class {self.class_no} - {self.section}"
