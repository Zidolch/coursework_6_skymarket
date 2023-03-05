from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    message = 'У Вас недостаточно прав.'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.is_admin:
            return True
        return False
