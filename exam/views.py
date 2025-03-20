from django.shortcuts import get_object_or_404, redirect, render

from .models import Exam


def add_exam(request):
    exam_choices = Exam.EXAM_CHOICES
    time_choices = Exam.TIME_CHOICES
    exams = Exam.objects.all()  # Fetch all exams from the database

    if request.method == "POST":
        exam_name = request.POST.get("exam_name")
        exam_date = request.POST.get("exam_date")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")

        # Save to database
        Exam.objects.create(
            exam_name=exam_name,
            exam_date=exam_date,
            start_time=start_time,
            end_time=end_time,
        )
        return redirect("add_exam")  # Change to your exam listing view

    return render(
        request,
        "admin_panel/add_exam.html",
        {"exams": exams, "exam_choices": exam_choices, "time_choices": time_choices},
    )


def delete_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    exam.delete()
    return redirect("manage_exams")


def edit_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)

    if request.method == "POST":
        exam.exam_name = request.POST.get("exam_name")
        exam.exam_date = request.POST.get("exam_date")
        exam.start_time = request.POST.get("start_time")
        exam.end_time = request.POST.get("end_time")
        exam.save()
        return redirect("add_exam")

    return render(
        request,
        "admin_panel/edit_exam.html",
        {
            "exam": exam,
            "exam_choices": Exam.EXAM_CHOICES,
            "time_choices": Exam.TIME_CHOICES,
        },
    )


def teacher_view_exam(request):
    exams = Exam.objects.all()
    return render(request, "teacher/view_exam.html", {"exams": exams})


def student_view_exam(request):
    exams = Exam.objects.all()
    return render(request, "student/view_exam.html", {"exams": exams})
