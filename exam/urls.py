from django.urls import path

from . import views

urlpatterns = [
    path("add-exam/", views.add_exam, name="add_exam"),
    path("delete-exam/<int:exam_id>/", views.delete_exam, name="delete_exam"),
    path("edit-exam<int:exam_id>/", views.edit_exam, name="edit_exam"),
    path("teacher-view-exam/", views.teacher_view_exam, name="teacher_view_exam"),
    path("student-view-exam/", views.student_view_exam, name="student_view_exam"),
]
