from django.urls import path

from .views import (
    add_student,
    add_teacher,
    admin_dashboard,
    manage_students,
    manage_teachers,
)

urlpatterns = [
    path("dashboard/", admin_dashboard, name="admin_dashboard"),
    path("add-student/", add_student, name="add_student"),
    path("manage-students/", manage_students, name="manage_students"),
    path("add-teacher/", add_teacher, name="add_teacher"),
    path("manage-teachers/", manage_teachers, name="manage_teachers"),
]
