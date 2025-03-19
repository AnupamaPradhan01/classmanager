from django.urls import path

from . import views

urlpatterns = [
    path("mark-attendance/", views.mark_attendance, name="mark_attendance"),
    path("list-attendance/", views.list_attendance, name="list_attendance"),
    path(
        "edit-attendance/",
        views.edit_attendance,
        name="edit_attendance",
    ),
    path(
        "view-attendance/",
        views.view_attendance_student_dashboard,
        name="view_attendance_student_dashboard",
    ),
    path(
        "view-teacher-attendance/",
        views.view_teacher_attendance,
        name="view_teacher_attendance",
    ),
    path(
        "mark-teacher-attendance/",
        views.mark_teacher_attendance,
        name="mark_teacher_attendance",
    ),
    path(
        "edit-teacher-attendance/",
        views.edit_teacher_attendance,
        name="edit_teacher_attendance",
    ),
    path(
        "my-attendance/",
        views.view_attendance_teacher_dashboard,
        name="my_attendance",
    ),
]
