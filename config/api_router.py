from rest_framework.routers import DefaultRouter

from apps.employees.api.views import DepartmentViewSet, EmployeeViewSet

router = DefaultRouter()

router.register("employees", EmployeeViewSet)
router.register("departments", DepartmentViewSet)

app_name = "api"
urlpatterns = router.urls
