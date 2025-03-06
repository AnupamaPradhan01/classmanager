from django.urls import path

from . import views
from .views import delete_exam, delete_timetable, edit_exam, edit_timetable

urlpatterns = [
    path("dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("profile/", views.view_teacher_profile, name="profile"),
    path("profile/edit/", views.edit_teacher_profile, name="edit_profile"),
    path("manage-timetable/", views.manage_timetable, name="manage_timetable"),
    path("mark-attendance/", views.mark_attendance, name="mark_attendance"),
    path("create-assignment/", views.create_assignment, name="create_assignment"),
    path("review-assignments/", views.review_assignments, name="review_assignments"),
    path(
        "grade-submission/<int:submission_id>/",
        views.grade_submission,
        name="grade_submission",
    ),
    path("manage-exams/", views.manage_exams, name="manage_exams"),
    path(
        "manage-exam-papers/<int:exam_id>/",
        views.manage_exam_papers,
        name="manage_exam_papers",
    ),
    path("edit-exam/<int:exam_id>/", edit_exam, name="edit_exam"),
    path("delete-exam/<int:exam_id>/", delete_exam, name="delete_exam"),
    path("edit_timetable/<int:timetable_id>/", edit_timetable, name="edit_timetable"),
    path(
        "delete_timetable/<int:timetable_id>/",
        delete_timetable,
        name="delete_timetable",
    ),
]
