import calendar
from datetime import date, datetime

from attendance.models import Attendance
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from student.models import Student
from teacher.models import Teacher


@login_required
def mark_attendance(request):
    # Get the logged-in teacher
    teacher = Teacher.objects.get(user=request.user)

    # Fetch students assigned to this teacher
    students = Student.objects.filter(
        student_class=teacher.class_assigned, section=teacher.section
    )

    if request.method == "POST":
        for student in students:
            attendance_status = request.POST.get(f"attendance_{student.id}")
            if attendance_status:
                # Save attendance
                Attendance.objects.update_or_create(
                    student=student,
                    teacher=teacher,
                    date=date.today(),
                    defaults={"status": attendance_status},
                )
        # messages.success(request, "Attendance marked successfully!")
        return redirect("mark_attendance")

    return render(request, "teacher/mark_attendance.html", {"students": students})


def list_attendance(request):

    # Get distinct years
    available_years = list(
        Attendance.objects.dates("date", "year", order="DESC").values_list(
            "date", flat=True
        )
    )
    available_years = [y.year for y in available_years]  # Convert to list of years

    # Default to most recent year
    selected_year = int(
        request.GET.get(
            "year", max(available_years) if available_years else datetime.now().year
        )
    )
    selected_month = int(request.GET.get("month", datetime.now().month))

    # Get months with attendance records for the selected year
    available_months = list(
        Attendance.objects.filter(date__year=selected_year)
        .dates("date", "month", order="DESC")
        .values_list("date", flat=True)
    )
    available_months = [m.month for m in available_months]

    # Get days in the selected month
    num_days = calendar.monthrange(selected_year, selected_month)[1]
    days = list(range(1, num_days + 1))

    # Fetch attendance records
    attendance_records = Attendance.objects.filter(
        date__year=selected_year, date__month=selected_month
    )

    # Structure attendance data
    attendance_data = []
    students = set(record.student for record in attendance_records)

    for student in students:
        student_name = f"{student.first_name} {student.last_name}"
        row = [student_name]

        status_dict = {
            record.date.day: record.status
            for record in attendance_records
            if record.student == student
        }

        for day in days:
            row.append(status_dict.get(day, "-"))

        attendance_data.append(row)

    return render(
        request,
        "teacher/list_attendance.html",
        {
            "attendance_data": attendance_data,
            "selected_month": selected_month,
            "selected_year": selected_year,
            "days": days,
            "year_range": available_years,  # Ensure correct context key
            "months": available_months,  # Ensure correct context key
        },
    )


def update_attendance(request):
    if request.method == "POST":
        student_name = request.POST.get("student.first_name")
        date = request.POST.get("date")
        status = request.POST.get("status")  # 'Present' or 'Absent'

        # Update the database
        record, created = Attendance.objects.get_or_create(
            student__name=student_name, date=date
        )
        record.status = status
        record.save()

        return JsonResponse(
            {"success": True, "message": "Attendance updated successfully!"}
        )
    return JsonResponse({"success": False, "message": "Invalid request"})
