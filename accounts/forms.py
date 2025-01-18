from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ["username", "email", "role", "password1", "password2"]

        # You can also define the widgets for placeholders here.
        widgets = {
            "username": forms.TextInput(
                attrs={"placeholder": "Enter your username", "class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "Enter your email", "class": "form-control"}
            ),
            "role": forms.Select(
                attrs={"class": "form-control"}
            ),  # You may not need a placeholder for Select fields
            "password1": forms.PasswordInput(
                attrs={"placeholder": "Enter your password", "class": "form-control"}
            ),
            "password2": forms.PasswordInput(
                attrs={"placeholder": "Confirm your password", "class": "form-control"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ensure placeholders appear for password fields
        self.fields["password1"].widget.attrs["placeholder"] = "Enter your password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm your password"
        self.fields["email"].widget.attrs["placeholder"] = "Enter your email"
