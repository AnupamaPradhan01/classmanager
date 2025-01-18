from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.monitor_dashboard, name="monitor_dashboard"),
]
