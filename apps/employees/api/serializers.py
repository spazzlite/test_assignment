from rest_framework import serializers

from apps.employees.models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class EmployeeQueryParamsSerializer(serializers.Serializer):
    department_id = serializers.IntegerField(required=False)
    surname = serializers.CharField(required=False)


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class DepartmentListSerializer(serializers.ModelSerializer):
    employees_count = serializers.IntegerField()
    salary_sum = serializers.IntegerField()

    class Meta:
        model = Department
        fields = ('id', 'name', 'employees_count', 'salary_sum')
