from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def monitor_dashboard(request):
    return render(request, "monitor/dashboard.html", {"user": request.user})
