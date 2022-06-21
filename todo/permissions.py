from rest_framework import permissions


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and hasattr(request.user, 'employee'))

