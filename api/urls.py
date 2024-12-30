from django.urls import path, include


urlpatterns = [
    path("student/", include("api.student.urls")),
    path("department/", include("api.department.urls")),
    path("instructor/", include("api.instructor.urls")),
]
