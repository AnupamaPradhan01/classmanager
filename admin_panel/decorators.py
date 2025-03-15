from functools import wraps

from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden

User = get_user_model()


def admin_required(view_func):
    """Decorator to allow only admin users to access a view."""

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        if user.role == "admin" or user.role == "Admin":
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You do not have permission to access this page.")

    return _wrapped_view
