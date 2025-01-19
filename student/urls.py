from django.urls import path

from . import views
from .views import view_attendance

urlpatterns = [
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
    path("attendance/", view_attendance, name="view_attendance"),
    path("view-timetable/", views.view_timetable, name="view_timetable"),
]
