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
            return redirect("dashboard")  # Redirect after login
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
            return redirect("dashboard")
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
def dashboard(request):
    if request.user.role == "teacher":
        return render(request, "accounts/teacher_dashboard.html")
    elif request.user.role == "student":
        return render(request, "accounts/student_dashboard.html")
    elif request.user.role == "monitor":
        return render(request, "accounts/monitor_dashboard.html")
    elif request.user.role == "parent":
        return render(request, "accounts/parent_dashboard.html")
    else:
        return redirect("login")
