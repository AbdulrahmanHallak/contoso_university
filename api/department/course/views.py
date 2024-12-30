from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from api.models import Department, Course
from .serializers import CourseSerializer


class DepartmentCoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # TODO: check if you can modify the lookup_url_kwarg and lookup
    def get_queryset(self):
        department_id = self.kwargs.get("department_pk")
        if department_id:
            return super().get_queryset().filter(department__id=department_id)
        return super().get_queryset()

    def perform_create(self, serializer):
        department_id = self.kwargs.get("department_pk")
        department = get_object_or_404(Department, pk=department_id)
        serializer.save(department=department)
