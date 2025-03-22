from assignment.models import TeacherAssignment
from attendance.models import Attendance
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from exam.models import Exam
from student.models import Student

from .models import Teacher


@login_required
def teacher_dashboard(request):
    teacher = Teacher.objects.get(email=request.user)
    fname = teacher.first_name
    lname = teacher.last_name
    profile_pic = teacher.teacher_photo.url
    student_count = Student.objects.filter(student_class=teacher.class_assigned).count()
    assignment_count = TeacherAssignment.objects.filter(teacher=teacher).count()
    exam_count = Exam.objects.all().count()
    attendance_count = Attendance.objects.filter(
        teacher=teacher, status="Present"
    ).count()
    return render(
        request,
        "teacher/dashboard.html",
        {
            "user": request.user,
            "first_name": fname,
            "last_name": lname,
            "profile_pic": profile_pic,
            "student_count": student_count,
            "assignment_count": assignment_count,
            "exam_count": exam_count,
            "attendance_count": attendance_count,
        },
    )


@login_required
def view_profile(request):
    teacher = Teacher.objects.get(email=request.user)
    return render(request, "teacher/view_profile.html", {"teacher": teacher})
    return render(request, "teacher/view_profile.html", {"teacher": teacher})
    return render(request, "teacher/view_profile.html", {"teacher": teacher})
