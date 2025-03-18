from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Teacher


@login_required
def teacher_dashboard(request):
    teacher = Teacher.objects.get(email=request.user)
    fname = teacher.first_name
    lname = teacher.last_name
    profile_pic = teacher.teacher_photo.url
    return render(
        request,
        "teacher/dashboard.html",
        {
            "user": request.user,
            "first_name": fname,
            "last_name": lname,
            "profile_pic": profile_pic,
        },
    )


@login_required
def view_profile(request):
    teacher = Teacher.objects.get(email=request.user)
    return render(request, "teacher/view_profile.html", {"teacher": teacher})
