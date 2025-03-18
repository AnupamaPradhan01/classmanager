from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Student


@login_required
def student_dashboard(request):
    student = Student.objects.get(email=request.user)
    fname = student.first_name
    lname = student.last_name
    profile_pic = student.student_photo.url

    return render(
        request,
        "student/dashboard.html",
        {
            "user": request.user,
            "first_name": fname,
            "last_name": lname,
            "profile_pic": profile_pic,
        },
    )


@login_required
def student_view_profile(request):
    student = Student.objects.get(email=request.user)
    return render(request, "student/view_profile.html", {"student": student})
