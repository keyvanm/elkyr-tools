from rest_framework import permissions


class IsHostOrReadOnly(permissions.BasePermission):
    """
    Permission for events: Read permissions are allowed to all users. Write permissions for hosts only
    """

    def has_object_permission(self, request, view, event):
        return request.method in permissions.SAFE_METHODS or event.host == request.user

