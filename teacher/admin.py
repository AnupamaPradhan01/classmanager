from django.contrib import admin

from .models import Attendance, Timetable


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ("class_name", "day", "subject", "time", "teacher")
    list_filter = ("class_name", "day", "teacher")
    search_fields = ("class_name", "subject", "teacher__username")
    ordering = ("day", "time")


admin.site.register(Attendance)
