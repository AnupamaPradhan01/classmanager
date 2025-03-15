from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm


# Register User
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return role_based_redirect(request)  # Redirect after login
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


# Login User
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return role_based_redirect(request)
        else:
            return render(
                request, "accounts/login.html", {"error": "Invalid credentials"}
            )
    return render(request, "accounts/login.html")


# Logout User
def user_logout(request):
    logout(request)
    return redirect("login")


# Dashboard - Role-based views
@login_required
def role_based_redirect(request):
    user = request.user
    if user.role == "student":
        return redirect("student_dashboard")
    elif user.role == "teacher":
        return redirect("teacher_dashboard")
    elif user.role == "parent":
        return redirect("parent_dashboard")
    elif user.role == "admin":
        return redirect("admin_dashboard")
    else:
        return redirect("login")


def home(request):
    return render(request, "accounts/home.html")
