from admin_panel.decorators import admin_required
from django.shortcuts import redirect, render
from student.models import Student
from teacher.models import CLASS_CHOICES, SECTION_CHOICES
from timetable.models import Timetable


@admin_required
def add_timetable(request):
    if request.method == "POST":
        class_no = request.POST.get("class_no")
        section = request.POST.get("section")
        timetable_file = request.FILES.get("timetable_file")

        print(class_no, section, timetable_file)

        if timetable_file and timetable_file.name.endswith((".xls", ".xlsx")):
            print("hello")
            Timetable.objects.create(
                class_no=class_no, section=section, timetable_file=timetable_file
            )
            return redirect("admin_dashboard")  # Redirect after successful upload
    else:
        return render(
            request,
            "admin_panel/add_timetable.html",
            {"CLASS_CHOICES": CLASS_CHOICES, "SECTION_CHOICES": SECTION_CHOICES},
        )


def student_view_timetable(request):

    import pandas as pd

    student = Student.objects.get(email=request.user)
    class_no = student.student_class
    section = student.section

    timetable = Timetable.objects.filter(class_no=class_no, section=section).first()
    timetable_download_path = timetable.timetable_file.url
    timetable_path = timetable.timetable_file.path

    # Read the Excel file
    df = pd.read_excel(timetable_path)

    # Convert DataFrame to a list of dictionaries
    timetable_data = df.to_dict(orient="records")

    return render(
        request,
        "student/view_timetable.html",
        {
            "timetable": timetable_data,
            "timetable_download_path": timetable_download_path,
        },
    )
