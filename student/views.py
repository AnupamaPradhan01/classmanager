from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from teacher.models import Assignment, Attendance, ExamSchedule, Submission, Timetable

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
def view_timetable(request):
    if request.user.role != "student":
        return redirect("dashboard")

    student_profile = request.user.student_profile
    timetables = Timetable.objects.filter(
        class_name=student_profile.class_name
    ).order_by("day", "time")

    return render(request, "student/timetable.html", {"timetables": timetables})


@login_required
def view_attendance_details(request):
    attendance_records = Attendance.objects.filter(student=request.user).order_by(
        "-date"
    )
    return render(
        request,
        "student/attendance_details.html",
        {"attendance_records": attendance_records},
    )


@login_required
def view_assignments(request):
    assignments = Assignment.objects.filter(
        class_name=request.user.student_profile.class_name
    )
    return render(
        request, "student/view_assignments.html", {"assignments": assignments}
    )


@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == "POST":
        submission_file = request.FILES.get("submission_file")
        if not submission_file:
            messages.error(request, "Please upload a file.")
            return redirect("submit_assignment", assignment_id=assignment.id)

        Submission.objects.create(
            assignment=assignment,
            student=request.user,
            submission_file=submission_file,
        )
        messages.success(request, "Assignment submitted successfully!")
        return redirect("view_assignments")
    return render(request, "student/submit_assignment.html", {"assignment": assignment})


@login_required
def view_exam_schedule(request):
    student_profile = request.user.student_profile
    exams = ExamSchedule.objects.filter(class_name=student_profile.class_name).order_by(
        "exam_date"
    )
    return render(request, "student/exam_schedule.html", {"exams": exams})


@login_required
def view_profile(request):
    return render(request, "student/exam_schedule.html")
