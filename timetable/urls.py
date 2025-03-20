from django.urls import path

from . import views

urlpatterns = [
    path("add-timetable/", views.add_timetable, name="add_timetable"),
    path(
        "student-view-timetable",
        views.student_view_timetable,
        name="student_view_timetable",
    ),
]
