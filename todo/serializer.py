from typing import Tuple

from rest_framework import serializers

from todo.models import Assignment, Employee


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = Tuple = (
            '__all__'
        )


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields: Tuple = (
            '__all__'
        )
