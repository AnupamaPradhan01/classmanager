# student/forms.py
from django import forms

from .models import StudentProfile


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = [
            "roll_number",
            "date_of_birth",
            "class_name",
            "section",
            "student_phone_number",
            "address",
            "parent_name",
            "parent_phone_number",
            "admission_date",
            "profile_photo",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "admission_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize form widgets if needed
        self.fields["profile_photo"].required = False  # Make the photo optional
