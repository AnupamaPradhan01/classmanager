from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from teacher.models import Timetable


@login_required
def student_dashboard(request):
    return render(request, "student/dashboard.html", {"user": request.user})


@login_required
def view_attendance(request):
    # Fetch attendance for the logged-in user
    # print("View attendance called")
    # attendance_records = Attendance.objects.filter(student=request.user).order_by(
    #     "-date"
    # )
    return render(request, "student/attendance_details.html")


@login_required
def view_timetable(request):
    """
    View to display the timetable for the logged-in student's class.
    """
    # Ensure the user has a class_name attribute (specific to your user model)
    if hasattr(request.user, "class_name") and request.user.class_name:
        timetables = Timetable.objects.filter(
            class_name=request.user.class_name
        ).order_by("day", "time")
    else:
        timetables = []  # No timetable to display if class_name is missing

    return render(request, "student/timetable.html", {"timetables": timetables})
