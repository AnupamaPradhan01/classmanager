from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
    # URL for viewing profile
    path("profile/", views.view_profile, name="view_profile"),
    # URL for editing the profile
    path("profile/edit/", views.edit_profile, name="edit_profile"),
]
