from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsInstructor, IsStudent
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet to perform CRUD operations on courses.
    - Instructors can Create, Update, and Delete courses.
    - Students can only list and retrieve courses.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsInstructor()]
        return [IsAuthenticated()]