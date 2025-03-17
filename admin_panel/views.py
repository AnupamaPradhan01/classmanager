from admin_panel.decorators import admin_required
from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from student.models import CLASS_CHOICES, GENDER_CHOICES, SECTION_CHOICES, Student
from teacher.models import (
    CLASS_CHOICES,
    GENDER_CHOICES,
    RELIGION_CHOICES,
    SECTION_CHOICES,
    SUBJECT_CHOICES,
    Teacher,
)

User = get_user_model()


@admin_required
def admin_dashboard(request):
    user = User.objects.get(username=request.user)
    if user.role.lower() == "admin":  # Handle case sensitivity
        total_students = Student.objects.count()
        total_teachers = Teacher.objects.count()
        # total_courses = Course.objects.count()
        # total_subjects = Subject.objects.count()

        context = {
            "user": request.user,
            "total_students": total_students,
            "total_teachers": total_teachers,
            # "total_courses": total_courses,
            # "total_subjects": total_subjects,
        }
        return render(request, "admin_panel/dashboard.html", context)

    return render(request, "admin_panel/404error.html")


# View to register a new student
@admin_required
def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        student_class = request.POST.get("class")
        section = request.POST.get("section")
        roll = request.POST.get("roll")
        admission_no = request.POST.get("admission_no")
        religion = request.POST.get("religion")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        nationality = request.POST.get("nationality")
        present_address = request.POST.get("present_address")
        permanent_address = request.POST.get("permanent_address")
        father_name = request.POST.get("father_name")
        mother_name = request.POST.get("mother_name")
        father_occupation = request.POST.get("father_occupation")
        mother_occupation = request.POST.get("mother_occupation")
        student_photo = request.FILES.get("student_photo")
        parent_photo = request.FILES.get("parent_photo")

        user = User.objects.create(
            username=email,  # Assuming email is unique
            email=email,
            role="student",  # Assign student role
        )
        password = f"{first_name.lower()}{last_name.lower()}"
        user.set_password(password)
        user.save()

        student = Student.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=dob,
            student_class=student_class,
            section=section,
            admission_number=admission_no,
            roll_number=roll,
            religion=religion,
            email=email,
            phone_number=phone_number,
            nationality=nationality,
            present_address=present_address,
            permanent_address=permanent_address,
            father_name=father_name,
            mother_name=mother_name,
            father_occupation=father_occupation,
            mother_occupation=mother_occupation,
            student_photo=student_photo,
            parent_photo=parent_photo,
        )

        return redirect(
            "admin_dashboard"
        )  # Redirect to a student list page or success page

    return render(
        request,
        "admin_panel/add_student.html",
        {
            "class_choices": CLASS_CHOICES,
            "section_choices": SECTION_CHOICES,
            "gender_choices": GENDER_CHOICES,
        },
    )


@admin_required
def manage_students(request):
    from django.conf import settings

    students = Student.objects.all()
    media_url = settings.MEDIA_URL
    return render(
        request,
        "admin_panel/manage_student.html",
        {"students": students, "MEDIA_URL": media_url},
    )


@admin_required
def edit_student(request, id):
    student = Student.objects.get(id=id)  # Fetch student record

    if request.method == "POST":
        # Update fields manually
        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.gender = request.POST.get("gender")
        student.date_of_birth = request.POST.get("date_of_birth")
        student.phone_number = request.POST.get("phone_number")
        student.email = request.POST.get("email")
        student.student_class = request.POST.get("student_class")
        student.section = request.POST.get("section")
        student.roll_number = request.POST.get("roll_number")
        student.admission_number = request.POST.get("admission_number")
        student.present_address = request.POST.get("present_address")
        student.permanent_address = request.POST.get("permanent_address")
        student.father_name = request.POST.get("father_name")
        student.father_occupation = request.POST.get("father_occupation")
        student.mother_name = request.POST.get("mother_name")
        student.mother_occupation = request.POST.get("mother_occupation")

        # Handle photo uploads
        if "student_photo" in request.FILES:
            student.student_photo = request.FILES["student_photo"]
        if "parent_photo" in request.FILES:
            student.parent_photo = request.FILES["parent_photo"]

        student.save()  # Save the changes
        return redirect("manage_students")  # Redirect to student list
    return render(request, "admin_panel/edit_student.html", {"student": student})


@admin_required
def delete_student(request, id):
    student = Student.objects.get(id=id)
    if student is not None:
        student.delete()
        return redirect("manage_students")
    else:
        return HttpResponseBadRequest("Data does not exists.")


# view to add a new teacher
@admin_required
def add_teacher(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        religion = request.POST.get("religion")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone_no")
        address = request.POST.get("address")
        id_no = request.POST.get("id_no")
        class_assigned = request.POST.get("class_assigned")
        section = request.POST.get("section")
        subject = request.POST.get("subject")
        teacher_photo = request.FILES.get("teacher_photo")

        print("Checking for existing user with email:", email)  # Debugging

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            print("User with this email already exists")  # Debugging
            # messages.error(request, "A user with this email already exists.")
            # return redirect("add_teacher")
        user = User.objects.create(
            username=email,  # Assuming email is unique
            email=email,
            role="teacher",  # assign teacher role
        )
        password = f"{first_name.lower()}{last_name.lower()}"
        user.set_password(password)
        user.save()

        # Save to database
        Teacher.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=dob,
            religion=religion,
            email=email,
            phone_no=phone_no,
            address=address,
            id_no=id_no,
            class_assigned=class_assigned,
            section=section,
            subject=subject,
            teacher_photo=teacher_photo,
        )

        # messages.success(request, "Teacher added successfully!")
        return redirect("admin_dashboard")  # Redirect to the teacher list page

    return render(
        request,
        "admin_panel/add_teacher.html",
        {
            "class_choices": CLASS_CHOICES,
            "section_choices": SECTION_CHOICES,
            "gender_choices": GENDER_CHOICES,
            "subject_choices": SUBJECT_CHOICES,
            "religion_choices": RELIGION_CHOICES,
        },
    )


@admin_required
def manage_teachers(request):
    from django.conf import settings

    teachers = Teacher.objects.all()
    media_url = settings.MEDIA_URL
    return render(
        request,
        "admin_panel/manage_teacher.html",
        {"teachers": teachers, "MEDIA_URL": media_url},
    )


@admin_required
def edit_teacher(request, id):
    teacher = Teacher.objects.get(id=id)  # Fetch student record

    if request.method == "POST":
        # Update fields manually
        teacher.first_name = request.POST.get("first_name")
        teacher.last_name = request.POST.get("last_name")
        teacher.gender = request.POST.get("gender")
        teacher.date_of_birth = request.POST.get("date_of_birth")
        teacher.religion = request.POST.get("religion")
        teacher.email = request.POST.get("email")
        teacher.phone_no = request.POST.get("phone_no")
        teacher.address = request.POST.get("address")
        teacher.id_no = request.POST.get("id_no")
        teacher.class_assigned = request.POST.get("class_assigned")
        teacher.section = request.POST.get("section")
        teacher.subject = request.POST.get("subject")

        # Handle photo uploads
        if "teacher_photo" in request.FILES:
            teacher.teacher_photo = request.FILES["teacher_photo"]

        teacher.save()  # Save the changes
        return redirect("manage_teachers")  # Redirect to student list
    return render(request, "admin_panel/edit_teacher.html", {"teacher": teacher})


@admin_required
def delete_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    if teacher is not None:
        teacher.delete()
        return redirect("manage_teachers")
    else:
        return HttpResponseBadRequest("Data does not exists.")


def add_timetable(request):
    return render(request, "admin_panel/add_timetable.html")
