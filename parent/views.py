from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def parent_dashboard(request):
    return render(request, "parent/dashboard.html", {"user": request.user})
