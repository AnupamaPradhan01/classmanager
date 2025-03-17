from .models import Student


def admin_profile(request):
    if request.user.is_authenticated:
        try:
            student = user.objects.get(email=request.user.email)
            return {
                "profile_pic": (
                    student.student_photo.url if student.student_photo else None
                ),
                "first_name": student.first_name,
                "last_name": student.last_name,
            }
        except Student.DoesNotExist:
            return {}  # If no student is found, return an empty dictionary
    return {}  # If user is not authenticated, return an empty dictionary
