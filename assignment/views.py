from assignment.models import StudentAssignmentUpload, TeacherAssignment
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from student.models import Student
from teacher.models import CLASS_CHOICES, SECTION_CHOICES, Teacher


@login_required
def teacher_add_assignment(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        class_nu = request.POST.get("class_nu")
        section = request.POST.get("section")
        deadline = request.POST.get("deadline")
        file = request.FILES.get("file")
        teacher = Teacher.objects.get(email=request.user)

        TeacherAssignment.objects.create(
            title=title,
            description=description,
            class_nu=class_nu,
            section=section,
            deadline=deadline,
            file=file,
            teacher=teacher,
        )
        return redirect("teacher_add_assignment")

    assignments = TeacherAssignment.objects.filter(
        teacher=Teacher.objects.get(email=request.user)
    )
    return render(
        request,
        "teacher/add_assignment.html",
        {
            "CLASS_CHOICES": CLASS_CHOICES,
            "SECTION_CHOICES": SECTION_CHOICES,
            "assignments": assignments,
        },
    )


@login_required
def student_view_assignment(request):
    student = get_object_or_404(Student, email=request.user)

    # Fetch all assignments for the student's class and section
    assignments = TeacherAssignment.objects.filter(
        class_nu=student.student_class, section=student.section
    )

    # Fetch assignments the student has already uploaded
    uploaded_assignments = StudentAssignmentUpload.objects.filter(
        student=student
    ).values_list("assignment_id", flat=True)

    return render(
        request,
        "student/view_assignment.html",
        {
            "assignments": assignments,
            "uploaded_assignments": list(uploaded_assignments),
        },
    )


@login_required
def student_upload_assignment(request, assignment_id):
    assignment = get_object_or_404(TeacherAssignment, id=assignment_id)
    student = get_object_or_404(Student, user=request.user)  # Get the logged-in student

    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        StudentAssignmentUpload.objects.create(
            assignment=assignment, student=student, file=uploaded_file
        )
        return redirect("student_dashboard")  # Redirect to the student's dashboard

    return redirect("assignments_list")  # Redirect if no file is uploaded


@login_required
def teacher_view_student_assignments(request, assignment_id):
    assignment = get_object_or_404(TeacherAssignment, id=assignment_id)
    submissions = StudentAssignmentUpload.objects.filter(assignment=assignment)

    return render(
        request, "teacher/view_submissions.html", {"submissions": submissions}
    )
