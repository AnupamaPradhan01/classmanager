from django.contrib import admin

from .models import Attendance, ExamSchedule, TeacherProfile, Timetable


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", "subject_specialization", "assigned_classes")
    fields = (
        "user",
        "full_name",
        "subject_specialization",
        "assigned_classes",
    )  # Make fields editable


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ("class_name", "day", "subject", "time", "teacher")
    list_filter = ("class_name", "day", "teacher")
    search_fields = ("class_name", "subject", "teacher__username")
    ordering = ("day", "time")


admin.site.register(Attendance)


@admin.register(ExamSchedule)
class ExamScheduleAdmin(admin.ModelAdmin):
    list_display = ["class_name", "subject", "exam_date", "start_time", "end_time"]
    ordering = ["exam_date", "class_name"]
