import calendar
from datetime import date, datetime

from attendance.models import Attendance, Teacher_Attendance
from django.contrib.auth.decorators import login_required
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


@login_required
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


@login_required
def edit_attendance(request):
    if request.method == "POST":
        student_roll = request.POST.get("student_roll")
        date = request.POST.get("date")
        status = request.POST.get("status")

        student = Student.objects.get(roll_number=student_roll)
        attendance_record = None

        if student:
            attendance_record = Attendance.objects.filter(
                student=student, date=date
            ).first()

        if attendance_record:
            attendance_record.status = status
            attendance_record.save()
        else:
            Attendance.objects.create(
                student=student,
                date=date,
                teacher=Teacher.objects.get(email=request.user),
                status=status,
            )

        return redirect("list_attendance")

    status_list = Attendance.ATTENDANCE_CHOICES
    att_status = [x[0] for x in status_list]
    return render(request, "teacher/edit_attendance.html", {"att_status": att_status})


@login_required
def view_attendance_student_dashboard(request):
    student_attendance = Attendance.objects.filter(
        student=Student.objects.get(email=request.user)
    )

    status_colors = {
        "Present": "green",
        "Late": "orange",
        "Absent": "red",
        "Holiday": "blue",
        "Halfday": "purple",
    }

    attendance_data = [
        {
            "title": att.status,  # Status (Present, Absent, etc.)
            "start": att.date.strftime("%Y-%m-%d"),  # Date format for FullCalendar
            "color": status_colors.get(att.status, "gray"),  # Get color based on status
        }
        for att in student_attendance
    ]

    return render(
        request, "student/view_attendance.html", {"attendance_data": attendance_data}
    )


@login_required
def view_teacher_attendance(request):

    # Get distinct years
    available_years = list(
        Teacher_Attendance.objects.dates("date", "year", order="DESC").values_list(
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
        Teacher_Attendance.objects.filter(date__year=selected_year)
        .dates("date", "month", order="DESC")
        .values_list("date", flat=True)
    )
    available_months = [m.month for m in available_months]

    # Get days in the selected month
    num_days = calendar.monthrange(selected_year, selected_month)[1]
    days = list(range(1, num_days + 1))

    # Fetch attendance records
    attendance_records = Teacher_Attendance.objects.filter(
        date__year=selected_year, date__month=selected_month
    )

    # Structure attendance data
    attendance_data = []
    teachers = set(record.teacher for record in attendance_records)

    for teacher in teachers:
        teacher_name = f"{teacher.first_name} {teacher.last_name}"
        row = [teacher_name]

        status_dict = {
            record.date.day: record.status
            for record in attendance_records
            if record.teacher == teacher
        }

        for day in days:
            row.append(status_dict.get(day, "-"))

        attendance_data.append(row)

    return render(
        request,
        "admin_panel/view_teacher_attendance.html",
        {
            "attendance_data": attendance_data,
            "selected_month": selected_month,
            "selected_year": selected_year,
            "days": days,
            "year_range": available_years,  # Ensure correct context key
            "months": available_months,  # Ensure correct context key
        },
    )


@login_required
def mark_teacher_attendance(request):
    teachers = Teacher.objects.all()

    if request.method == "POST":
        for teacher in teachers:
            attendance_status = request.POST.get(f"attendance_{teacher.id}")
            if attendance_status:
                Teacher_Attendance.objects.update_or_create(
                    teacher=teacher,
                    date=date.today(),
                    defaults={"status": attendance_status},
                )
        return redirect("view_teacher_attendance")

    return render(
        request, "admin_panel/mark_teacher_attendance.html", {"teachers": teachers}
    )


@login_required
def edit_teacher_attendance(request):

    if request.method == "POST":
        teacher_id = request.POST.get("teacher_id")
        date = request.POST.get("date")
        status = request.POST.get("status")

        teacher = Teacher.objects.get(id_no=teacher_id)
        attendance_record = None

        if teacher:
            attendance_record = Teacher_Attendance.objects.filter(
                teacher=teacher, date=date
            ).first()

        if attendance_record:
            attendance_record.status = status
            attendance_record.save()
        else:
            Teacher_Attendance.objects.create(
                teacher=teacher,
                date=date,
                status=status,
            )

        return redirect("view_teacher_attendance")

    status_list = Attendance.ATTENDANCE_CHOICES
    att_status = [x[0] for x in status_list]
    return render(
        request, "admin_panel/edit_teacher_attendance.html", {"att_status": att_status}
    )


@login_required
def view_attendance_teacher_dashboard(request):

    teacher_attendance = Teacher_Attendance.objects.filter(
        teacher=Teacher.objects.get(email=request.user)
    )

    status_colors = {
        "Present": "green",
        "Late": "orange",
        "Absent": "red",
        "Holiday": "blue",
        "Halfday": "purple",
    }

    attendance_data = [
        {
            "title": att.status,  # Status (Present, Absent, etc.)
            "start": att.date.strftime("%Y-%m-%d"),  # Date format for FullCalendar
            "color": status_colors.get(att.status, "gray"),  # Get color based on status
        }
        for att in teacher_attendance
    ]

    return render(
        request, "teacher/my_attendance.html", {"attendance_data": attendance_data}
    )
