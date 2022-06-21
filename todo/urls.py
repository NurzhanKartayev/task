from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSet, AssignmentViewSet

app_name = 'todo'
router = DefaultRouter()

router.register(
    prefix=r'employee', viewset=EmployeeViewSet, basename='employee'
)

router.register(
    prefix=r'assignment', viewset=AssignmentViewSet, basename='assignment'
)

urlpatterns = router.urls
