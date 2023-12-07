from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1 import views


router = DefaultRouter()
router.register('employee-API', views.EmployeeModelViewSet, basename="EMPLOYEE")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
