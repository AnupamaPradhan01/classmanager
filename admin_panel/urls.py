from django.urls import path

from .views import add_student, admin_dashboard

urlpatterns = [
    path("dashboard/", admin_dashboard, name="admin_dashboard"),
    path("add-student/", add_student, name="add_student"),
]
