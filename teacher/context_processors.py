from .models import Teacher


def teacher_profile(request):
    if request.user.is_authenticated:
        try:
            teacher = Teacher.objects.get(email=request.user.email)
            return {
                "profile_pic": (
                    teacher.teacher_photo.url if teacher.teacher_photo else None
                ),
                "first_name": teacher.first_name,
                "last_name": teacher.last_name,
            }
        except Teacher.DoesNotExist:
            return {}  # If no student is found, return an empty dictionary
    return {}  # If user is not authenticated, return an empty dictionary
