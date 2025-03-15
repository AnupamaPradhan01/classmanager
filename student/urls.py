from django.urls import path

from . import views
from .views import student_profile

urlpatterns = [
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
    path("profile/", student_profile, name="student_profile"),
    # url path to view timetable
    path("timetable/", views.view_timetable, name="view_timetable"),
    path(
        "attendance-details/", views.view_attendance_details, name="attendance_details"
    ),
    path("view-assignments/", views.view_assignments, name="view_assignments"),
    path(
        "submit-assignment/<int:assignment_id>/",
        views.submit_assignment,
        name="submit_assignment",
    ),
    path("exam-schedule/", views.view_exam_schedule, name="view_exam_schedule"),
    path("profile/", views.view_profile, name="view_profile"),
]
