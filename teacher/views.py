from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from teacher.models import Assignment, Attendance, Submission, Timetable


@login_required
def teacher_dashboard(request):
    return render(request, "teacher/dashboard.html", {"user": request.user})


@login_required
def manage_timetable(request):
    # Ensure only teachers can access this view
    if not request.user.is_authenticated or request.user.role != "teacher":
        return redirect("login")

    if request.method == "POST":
        day = request.POST.get("day")
        subject = request.POST.get("subject")
        time = request.POST.get("time")
        class_name = request.POST.get("class_name")

        # Check for existing timetable conflicts
        existing_timetable = Timetable.objects.filter(
            teacher=request.user, day=day, time=time, class_name=class_name
        )
        if existing_timetable.exists():
            messages.error(
                request, "A timetable for this time and class already exists."
            )
        else:
            # Create new timetable entry
            Timetable.objects.create(
                teacher=request.user,
                day=day,
                subject=subject,
                time=time,
                class_name=class_name,
            )
            messages.success(request, "Timetable added successfully.")

        return redirect("manage_timetable")

    # Fetch and paginate timetables created by the teacher
    timetables = Timetable.objects.filter(teacher=request.user).order_by("day", "time")
    paginator = Paginator(timetables, 10)  # Show 10 timetables per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "teacher/manage_timetable.html", {"page_obj": page_obj})


@login_required
def mark_attendance(request):
    if request.method == "POST":
        student_id = request.POST["student"]
        status = request.POST["status"]
        subject = request.POST["subject"]
        class_name = request.POST["class_name"]

        student = CustomUser.objects.get(id=student_id)
        Attendance.objects.create(
            student=student,
            class_name=class_name,
            status=status,
            subject=subject,
            teacher=request.user,
        )
        return redirect("mark_attendance")

    students = CustomUser.objects.filter(role="student")
    classes = students.values_list("student_profile__class_name", flat=True).distinct()
    return render(
        request,
        "teacher/mark_attendance.html",
        {"students": students, "classes": classes},
    )


@login_required
def create_assignment(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")
        class_name = request.POST.get("class_name")

        Assignment.objects.create(
            teacher=request.user,
            title=title,
            description=description,
            deadline=deadline,
            class_name=class_name,
        )
        messages.success(request, "Assignment created successfully.")
        return redirect("teacher_dashboard")

    return render(request, "teacher/create_assignment.html")


@login_required
def review_assignments(request):
    assignments = Assignment.objects.filter(teacher=request.user)
    return render(
        request, "teacher/review_assignments.html", {"assignments": assignments}
    )


@login_required
def grade_submission(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    if request.method == "POST":
        grade = request.POST.get("grade")
        feedback = request.POST.get("feedback")
        submission.grade = grade
        submission.feedback = feedback
        submission.save()
        messages.success(request, "Submission graded successfully.")
        return redirect("review_assignments")

    return render(request, "teacher/grade_submission.html", {"submission": submission})
