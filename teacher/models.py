# student/models.py
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
SUBJECT_CHOICES = [
    ("Math", "Mathematics"),
    ("Science", "Science"),
    ("English", "English"),
    ("History", "History"),
    ("Geography", "Geography"),
    ("Physics", "Physics"),
    ("Chemistry", "Chemistry"),
    ("Biology", "Biology"),
    ("Computer", "Computer Science"),
]


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # Link to Django User model
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    religion = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15)
    address = models.TextField()
    id_no = models.CharField(max_length=50, unique=True)
    class_assigned = models.CharField(
        max_length=100, choices=CLASS_CHOICES
    )  # Or use a ForeignKey
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    teacher_photo = models.ImageField(
        upload_to="teacher_photos/", blank=True, null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
