from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("view-profile/", views.view_profile, name="view_profile"),
]
