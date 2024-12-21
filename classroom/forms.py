from django import forms
from django.contrib.auth.forms import UserCreationForm

from classmanager.classroom.models import Student, User


##User Login Form(applied to both student and teacher login)
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "answer"}),
            "roll_no": forms.NumberInput(attrs={"class": "answer"}),
            "phone": forms.NumberInput(attrs={"class": "answer"}),
            "email": forms.EmailInput(attrs={"class": "answer"}),
        }


## Student Registration Form
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "roll_no", "phone", "email"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "answer"}),
            "roll_no": forms.NumberInput(attrs={"class": "answer"}),
            "phone": forms.NumberInput(attrs={"class": "answer"}),
            "email": forms.EmailInput(attrs={"class": "answer"}),
        }
