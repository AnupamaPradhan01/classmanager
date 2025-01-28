# student/admin.py
from django.contrib import admin

from .models import StudentProfile


class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "roll_number",
        "class_name",
        "section",
        "date_of_birth",
        "student_phone_number",
        "address",
        "parent_name",
        "parent_phone_number",
        "admission_date",
        "profile_photo",
    )
    search_fields = (
        "user__username",
        "roll_number",
        "class_name",
        "section",
        "parent_name",
    )
    list_filter = ("class_name", "section", "admission_date")
    ordering = ("class_name", "section", "roll_number")

    # Fields to be displayed in the detail view
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "roll_number",
                    "date_of_birth",
                    "student_phone_number",
                    "class_name",
                    "section",
                )
            },
        ),
        (
            "Contact Info",
            {
                "fields": (
                    "address",
                    "parent_name",
                    "parent_phone_number",
                )
            },
        ),
        ("Additional Info", {"fields": ("admission_date", "profile_photo")}),
    )


admin.site.register(StudentProfile, StudentProfileAdmin)
