from rest_framework import permissions


class UpdateIfStaffPermission(permissions.BasePermission):
    """
    Custom permission to allow anyone to read (GET) but only admins to create (POST).
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # Typically GET, HEAD, OPTIONS
            return True
        return request.user and request.user.is_staff  # Allow POST for staff users
