from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

course_router = DefaultRouter()
course_router.register(viewset=views.DepartmentCoursesViewSet, prefix="")

urlpatterns = [
    path("", include(course_router.urls)),
]
