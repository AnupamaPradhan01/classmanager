from datetime import date

from attendance.models import Attendance
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from exam.models import Exam

from .models import Student


@login_required
def student_dashboard(request):
    student = Student.objects.get(email=request.user)
    fname = student.first_name
    lname = student.last_name
    profile_pic = student.student_photo.url
    attendance_count = Attendance.objects.filter(student=student).count()

    today = date.today()
    current_month = today.month
    current_year = today.year

    total_days = Attendance.objects.filter(
        student=student, date__year=current_year, date__month=current_month
    ).count()
    present_count = Attendance.objects.filter(
        student=student,
        date__year=current_year,
        date__month=current_month,
        status="Present",
    ).count()
    absent_count = Attendance.objects.filter(
        student=student,
        date__year=current_year,
        date__month=current_month,
        status="Absent",
    ).count()
    exam_count = Exam.objects.count()

    if total_days > 0:
        present_percentage = round((present_count / total_days) * 100, 2)
        absent_percentage = round((absent_count / total_days) * 100, 2)
    else:
        present_percentage = 0
        absent_percentage = 0

    return render(
        request,
        "student/dashboard.html",
        {
            "user": request.user,
            "first_name": fname,
            "last_name": lname,
            "profile_pic": profile_pic,
            "attendance_count": attendance_count,
            "present_count": present_count,
            "absent_count": absent_count,
            "absent_percentage": absent_percentage,
            "present_percentage": present_percentage,
            "exam_count": exam_count,
        },
    )


@login_required
def student_view_profile(request):
    student = Student.objects.get(email=request.user)
    return render(request, "student/view_profile.html", {"student": student})
    student = Student.objects.get(email=request.user)
    return render(request, "student/view_profile.html", {"student": student})
