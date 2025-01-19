from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .models import Timetable


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
