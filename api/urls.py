from django.urls import path, include


urlpatterns = [
    # path("department/", views.DepartmentListCreateView.as_view()),
    # path("department/<int:pk>/course/", views.CourseListCreateView.as_view()),
    path("student/", include("api.student.urls")),
    path("department/", include("api.department.urls")),
    path("instructor/", include("api.instructor.urls")),
]
