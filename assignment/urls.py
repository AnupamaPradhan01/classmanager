from django.urls import path

from . import views

urlpatterns = [
    path(
        "teacher-add-assignment/",
        views.teacher_add_assignment,
        name="teacher_add_assignment",
    ),
    path(
        "student-view-assigment/",
        views.student_view_assignment,
        name="student_view_assigment",
    ),
    path(
        "student-upload-assignment/<int:assignment_id>",
        views.student_upload_assignment,
        name="student_upload_assignment",
    ),
    path(
        "teacher-view-student-assignments/<int:assignment_id>",
        views.teacher_view_student_assignments,
        name="teacher_view_student_assignments",
    ),
]
