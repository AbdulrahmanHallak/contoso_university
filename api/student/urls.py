from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

student_router = DefaultRouter()
student_router.register("", views.StudentViewSet)
urlpatterns = [
    path("", include(student_router.urls)),
    path("<int:student_pk>/course/", views.create_student_enrollment),
    path("<int:student_pk>/course/<int:course_pk>/", views.delete_student_enrollment),
]
