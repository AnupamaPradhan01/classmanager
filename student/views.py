from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import StudentProfileForm
from .models import StudentProfile


@login_required
def edit_profile(request):
    profile, created = StudentProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = StudentProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(
                "view_profile"
            )  # Redirect to the profile view page after saving
    else:
        form = StudentProfileForm(instance=profile)

    return render(request, "student/edit_profile.html", {"form": form})


# student/views.py
@login_required
def view_profile(request):
    profile, created = StudentProfile.objects.get_or_create(user=request.user)
    return render(request, "student/view_profile.html", {"profile": profile})


@login_required
def student_dashboard(request):
    return render(request, "student/dashboard.html", {"user": request.user})
