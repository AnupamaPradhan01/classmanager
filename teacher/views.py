from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def teacher_dashboard(request):
    return render(request, "teacher/dashboard.html")
