from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("manage-timetable/", views.manage_timetable, name="manage_timetable"),
]
