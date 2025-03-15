from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Dropdown choices
CLASS_CHOICES = [
    ("Nursery", "Nursery"),
    ("KG", "KG"),
    ("1st", "1st"),
    ("2nd", "2nd"),
    ("3rd", "3rd"),
    ("4th", "4th"),
    ("5th", "5th"),
    ("6th", "6th"),
    ("7th", "7th"),
    ("8th", "8th"),
    ("9th", "9th"),
    ("10th", "10th"),
    ("11th", "11th"),
    ("12th", "12th"),
]

SECTION_CHOICES = [
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
]

GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
]

RELIGION_CHOICES = [
    ("Hindu", "Hindu"),
    ("Muslim", "Muslim"),
    ("Christian", "Christian"),
    ("Sikh", "Sikh"),
    ("Other", "Other"),
]


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # Link to Django User model
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()

    # Academic Information
    student_class = models.CharField(max_length=20, choices=CLASS_CHOICES)
    section = models.CharField(max_length=5, choices=SECTION_CHOICES)
    roll_number = models.PositiveIntegerField(unique=True)
    admission_number = models.CharField(max_length=50, unique=True)

    # Contact Details
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    nationality = models.CharField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField()

    # Parent Details
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=255)

    # File Uploads
    student_photo = models.ImageField(
        upload_to="student_photos/", blank=True, null=True
    )
    parent_photo = models.ImageField(upload_to="parent_photos/", blank=True, null=True)

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} - {self.student_class} {self.section}"
        )
