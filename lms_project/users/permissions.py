from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    """
    Custom permission to check if the user is a student.
    """
    def has_permission(self, request, view):
        return request.user.role == 'student'

class IsInstructor(BasePermission):
    """
    Custom permission to check if the user is an instructor.
    """
    def has_permission(self, request, view):
        return request.user.role == 'instructor'

class IsAdmin(BasePermission):
    """
    Custom permission to check if the user is an admin.
    """
    def has_permission(self, request, view):
        return request.user.role == 'admin'