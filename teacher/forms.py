from django import forms

from .models import ExamSchedule, TeacherProfile


class TeacherProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = [
            "full_name",
            "subject_specialization",
            "phone_number",
            "profile_photo",
        ]


class ExamPaperForm(forms.ModelForm):
    class Meta:
        model = ExamSchedule
        fields = ["question_paper"]
