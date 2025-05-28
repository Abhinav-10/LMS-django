from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsInstructor, IsStudent
from .models import Assignment, Submission
from .serializers import AssignmentSerializer, SubmissionSerializer
class AssignmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet to perform CRUD operations on assignments.
    - Instructors can create, update, and delete assignments.
    - Students can only view assignments.
    """
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsInstructor()]
        return [IsAuthenticated(), IsStudent()]

class SubmissionViewSet(viewsets.ModelViewSet):
    """
    ViewSet to perform CRUD operations on submissions.
    - Students can create, update, and delete their submissions.
    - Instructors can only view submissions.
    """
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsStudent()]
        return [IsAuthenticated(), IsInstructor()]