from django.contrib import admin

from apps.employees.models import Department, Employee

admin.site.register(Department)
admin.site.register(Employee)
