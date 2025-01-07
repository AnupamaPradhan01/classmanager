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

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",  # Custom related_name
        blank=True,
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",  # Custom related_name
        blank=True,
        help_text="Specific permissions for this user.",
    )

    def __str__(self):
        return self.username
