from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom user model with role choices
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("teacher", "Teacher"),
        ("student", "Student"),
        ("monitor", "Class Monitor"),
        ("parent", "Parent"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
