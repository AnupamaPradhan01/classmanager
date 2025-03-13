from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("rolebasedredirect/", views.role_based_redirect, name="role"),
    path("", views.home, name="home"),  # Home page URL
]
