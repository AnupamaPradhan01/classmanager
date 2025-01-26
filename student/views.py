from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def student_dashboard(request):
    return render(request, "student/dashboard.html", {"user": request.user})
