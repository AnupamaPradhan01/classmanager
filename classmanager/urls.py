"""
URL configuration for classmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),  # Django admin panel
    path("admin-panel/", include("admin_panel.urls")),  # Your custom admin panel
    path("student/", include("student.urls")),
    path("teacher/", include("teacher.urls")),
    path("", include("accounts.urls")),  # Home page at root URL
    path("accounts/", include("accounts.urls")),  # Other accounts URLs
    path("attendance/", include("attendance.urls")),
    path("exam/", include("exam.urls")),
    path("timetable/", include("timetable.urls")),
    path("assignment/", include("assignment.urls")),
]
if settings.DEBUG:  # Serve media files only in development mode
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]
    )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
