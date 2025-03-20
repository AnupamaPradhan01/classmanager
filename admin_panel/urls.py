from django.urls import path

from .views import (  # add_timetable,
    add_student,
    add_teacher,
    admin_dashboard,
    delete_student,
    delete_teacher,
    edit_student,
    edit_teacher,
    manage_students,
    manage_teachers,
)

urlpatterns = [
    path("dashboard/", admin_dashboard, name="admin_dashboard"),
    path("add-student/", add_student, name="add_student"),
    path("manage-students/", manage_students, name="manage_students"),
    path("edit-student/<int:id>/", edit_student, name="edit_student"),
    path("delete-student/<int:id>/", delete_student, name="delete_student"),
    path("add-teacher/", add_teacher, name="add_teacher"),
    path("manage-teachers/", manage_teachers, name="manage_teachers"),
    path("edit-teacher/<int:id>/", edit_teacher, name="edit_teacher"),
    path("delete-teacher/<int:id>/", delete_teacher, name="delete_teacher"),
    # path("add-timetable/", add_timetable, name="add_timetable"),
]
