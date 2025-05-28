from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStudent, IsInstructor, IsAdmin
from .models import Enrollment
from .serializers import EnrollmentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet to perform CRUD operations on enrollments.
    - Students can create enrollments.
    - Instructors and Admins can manage all enrollments.
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [IsAuthenticated(), IsStudent()]
        return [IsAuthenticated(), IsInstructor() | IsAdmin()]