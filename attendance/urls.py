from django.urls import path

from . import views

urlpatterns = [
    path("mark-attendance/", views.mark_attendance, name="mark_attendance"),
    path("list-attendance/", views.list_attendance, name="list_attendance"),
    path("update-attendance/", views.update_attendance, name="update_attendance"),
]
