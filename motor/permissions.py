from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read Only permissions
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author