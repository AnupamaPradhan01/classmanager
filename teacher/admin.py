from django.contrib import admin
from teacher.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    class Meta:
        list_display = "__all__"
