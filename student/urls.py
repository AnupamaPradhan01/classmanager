from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
    path(
        "student-view-profile/", views.student_view_profile, name="student_view_profile"
    ),
]
