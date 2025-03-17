from django.urls import path

from . import views
from .views import student_profile

urlpatterns = [
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
    path("profile/", student_profile, name="student_profile"),
    path("view-profile/", views.view_profile, name="view_profile"),
]
