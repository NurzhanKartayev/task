

from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from todo.models import Employee, Assignment
from todo.permissions import IsEmployee

from todo.serializer import EmployeeSerializer, AssignmentSerializer


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAdminUser]
    http_method_names = 'get'
    pagination_class = None


class AssignmentViewSet(ModelViewSet):
    serializer_class = AssignmentSerializer
    permission_classes = [IsAdminUser | IsEmployee]
    queryset = Assignment.objects.all()
    pagination_class = None

    def get_queryset(self):
        if self.request.user.is_superuser:
            return super().get_queryset()
        else:
            return super().get_queryset().filter(employee__user=self.request.user)

