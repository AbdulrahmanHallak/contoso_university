from django.urls import path

from . import views

urlpatterns = [
    # path("department/", views.DepartmentListCreateView.as_view()),
    # path("department/<int:pk>/course/", views.CourseListCreateView.as_view()),
    path("", views.StudentListCreateView.as_view()),
    path("<int:pk>/", views.StudentDetailsView.as_view()),
    path("<int:pk>/update", views.StudentUpdateView.as_view()),
]
