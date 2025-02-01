from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("manage-timetable/", views.manage_timetable, name="manage_timetable"),
    path("mark-attendance/", views.mark_attendance, name="mark_attendance"),
    path("create-assignment/", views.create_assignment, name="create_assignment"),
    path("review-assignments/", views.review_assignments, name="review_assignments"),
    path(
        "grade-submission/<int:submission_id>/",
        views.grade_submission,
        name="grade_submission",
    ),
]
