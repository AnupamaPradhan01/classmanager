from django.contrib import admin

from .models import CustomUser


# Register the model
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "role")  # Columns to display
    search_fields = ("username", "email")  # Enable search by username or email
    list_filter = ("role",)  # Filter by role


admin.site.register(CustomUser, CustomUserAdmin)
