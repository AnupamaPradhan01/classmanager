from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from teacher.forms import ExamPaperForm, ExamScheduleForm, TeacherProfileUpdateForm
from teacher.models import (
    Assignment,
    Attendance,
    ExamSchedule,
    Submission,
    TeacherProfile,
    Timetable,
)


@login_required
def view_teacher_profile(request):
    profile = get_object_or_404(TeacherProfile, user=request.user)
    return render(request, "teacher/profile.html", {"profile": profile})


@login_required
def edit_teacher_profile(request):
    profile = get_object_or_404(TeacherProfile, user=request.user)

    if request.method == "POST":
        form = TeacherProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Prevent modification of assigned subjects and classes
            form.instance.assigned_classes = profile.assigned_classes
            form.instance.subject_specialization = profile.subject_specialization
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = TeacherProfileUpdateForm(instance=profile)

    return render(request, "teacher/edit_profile.html", {"form": form})


@login_required
def teacher_dashboard(request):
    return render(request, "teacher/dashboard.html", {"user": request.user})

    # @login_required
    # def manage_timetable(request):
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


# @login_required
# def edit_timetable(request, timetable_id):
#     timetable = get_object_or_404(Timetable, id=timetable_id, teacher=request.user)

#     if request.method == "POST":
#         form = TimetableForm(request.POST, instance=timetable)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Timetable updated successfully.")
#             return redirect("manage_timetable")
#     else:
#         form = TimetableForm(instance=timetable)

#     return render(request, "teacher/edit_timetable.html", {"form": form})


# @login_required
# def delete_timetable(request, timetable_id):
#     timetable = get_object_or_404(Timetable, id=timetable_id, teacher=request.user)
#     timetable.delete()
#     messages.success(request, "Timetable deleted successfully.")
#     return redirect("manage_timetable")


@login_required
def mark_attendance(request):
    teacher_profile = getattr(request.user, "teacher_profile", None)

    if not teacher_profile:
        return render(
            request,
            "teacher/mark_attendance.html",
            {"error": "No assigned classes found."},
        )

    assigned_classes = teacher_profile.assigned_classes.split(
        ","
    )  # Convert CSV to list
    students = CustomUser.objects.filter(
        role="student", student_profile__class_name__in=assigned_classes
    )

    if request.method == "POST":
        class_name = request.POST["class_name"]
        subject = request.POST["subject"]
        status_data = request.POST.getlist("status")  # List of statuses

        selected_students = students.filter(student_profile__class_name=class_name)
        for i, student in enumerate(selected_students):
            Attendance.objects.create(
                student=student,
                class_name=class_name,
                status=status_data[i],  # Assign respective status
                subject=subject,
                teacher=request.user,
            )

        return redirect("mark_attendance")

    subjects = ["Math", "Science", "English"]  # Modify according to available subjects

    return render(
        request,
        "teacher/mark_attendance.html",
        {
            "students": students,
            "assigned_classes": assigned_classes,
            "subjects": subjects,
        },
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


@login_required
def manage_exams(request):
    teacher_profile = request.user.teacher_profile
    if request.method == "POST":
        class_name = request.POST.get("class_name")
        subject = request.POST.get("subject")
        exam_date = request.POST.get("exam_date")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        notes = request.POST.get("notes")
        if class_name not in teacher_profile.assigned_classes.split(","):
            messages.error(
                request, "You can only schedule exams for your assigned classes."
            )
            return redirect("manage_exams")

        ExamSchedule.objects.create(
            teacher=request.user,
            class_name=class_name,
            subject=subject,
            exam_date=exam_date,
            start_time=start_time,
            end_time=end_time,
            notes=notes,
        )
        return redirect("manage_exams")

    exams = ExamSchedule.objects.all().order_by("exam_date")
    return render(request, "teacher/manage_exams.html", {"exams": exams})


@login_required
def manage_exam_papers(request, exam_id):
    exam = get_object_or_404(ExamSchedule, id=exam_id)
    if request.method == "POST":
        form = ExamPaperForm(request.POST, request.FILES, instance=exam)
        if form.is_valid():
            form.save()
            return redirect("manage_exams")
    else:
        form = ExamPaperForm(instance=exam)
    return render(
        request, "teacher/manage_exam_paper.html", {"form": form, "exam": exam}
    )


def edit_exam(request, exam_id):
    exam = get_object_or_404(ExamSchedule, id=exam_id)

    if request.method == "POST":
        form = ExamScheduleForm(request.POST, request.FILES, instance=exam)
        if form.is_valid():
            form.save()
            messages.success(request, "Exam schedule updated successfully!")
            return redirect("manage_exams")
    else:
        form = ExamScheduleForm(instance=exam)

    return render(request, "teacher/edit_exam.html", {"form": form, "exam": exam})


def delete_exam(request, exam_id):
    exam = get_object_or_404(ExamSchedule, id=exam_id)

    if request.method == "POST":
        exam.delete()
        messages.success(request, "Exam deleted successfully!")
        return redirect("manage_exams")

    return render(request, "teacher/confirm_delete_exam.html", {"exam": exam})
