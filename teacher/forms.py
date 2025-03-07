from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Assignment, ExamSchedule, TeacherProfile, Timetable


class TeacherProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = [
            "full_name",
            "phone_number",
        ]  # Exclude 'subject_specialization' and 'assigned_classes'


class ExamPaperForm(forms.ModelForm):
    class Meta:
        model = ExamSchedule
        fields = ["question_paper"]


class ExamScheduleForm(forms.ModelForm):
    class Meta:
        model = ExamSchedule
        fields = [
            "class_name",
            "subject",
            "exam_date",
            "start_time",
            "end_time",
            "notes",
            "question_paper",
        ]


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ["day", "subject", "time", "class_name"]


class AssignmentForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())  # Enable CKEditor

    class Meta:
        model = Assignment
        fields = ["title", "description", "deadline", "class_name"]
