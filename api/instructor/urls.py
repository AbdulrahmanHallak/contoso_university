from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(viewset=views.InstructorViewSet, prefix="")

office_router = DefaultRouter()
office_router.register("", views.OfficeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("<int:pk>/office/", include(office_router.urls)),
    path("<int:pk>/course/", views.InstructorCoursesListView.as_view()),
    path("<int:instructor_pk>/course/<int:course_pk>", views.delete_instructor_course),
    # TODO: method post now allowed
    path("<int:instructor_pk>/course/", views.create_instructor_course),
]
