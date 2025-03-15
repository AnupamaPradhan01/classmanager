from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from student.models import CLASS_CHOICES, GENDER_CHOICES, SECTION_CHOICES, Student

User = get_user_model()


@login_required
def admin_dashboard(request):
    return render(request, "admin_panel/dashboard.html", {"user": request.user})


# View to register a new student


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
