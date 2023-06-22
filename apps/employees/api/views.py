from django.db.models import Count, Sum
from django.db.models.functions import Coalesce
from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.employees.api.serializers import EmployeeListSerializer, DepartmentListSerializer, \
    EmployeeQueryParamsSerializer
from apps.employees.models import Employee, Department


class DepartmentViewSet(GenericViewSet, ListModelMixin):
    serializer_class = DepartmentListSerializer
    pagination_class = None
    queryset = Department.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        return self.queryset.annotate(
            employees_count=Count('employees'),
            salary_sum=Coalesce(Sum('employees__salary'), 0)
        )

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class EmployeeViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    serializer_class = EmployeeListSerializer
    pagination_class = PageNumberPagination
    queryset = Employee.objects.all()

    def get_queryset(self):
        serializer = EmployeeQueryParamsSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        query_params = serializer.validated_data
        queryset = self.queryset

        if 'surname' in query_params:
            surname = query_params.pop('surname')
            query_params['surname__contains'] = surname

        return queryset.filter(**query_params)

    @extend_schema(parameters=[EmployeeQueryParamsSerializer, ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
