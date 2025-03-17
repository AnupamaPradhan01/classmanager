from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Student


@login_required
def student_profile(request):
    student = get_object_or_404(
        Student, user__username=request.user.username
    )  # Fetch student by username
    return render(request, "student/profile.html", {"student": student})


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
def view_profile(request):
    student = Student.objects.get(email=request.user)
    return render(request, "student/view_profile.html", {"student": student})
