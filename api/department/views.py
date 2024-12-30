from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

from api.models import Department, Instructor
from .serializers import DepartmentSerializer, DepartmentInstructorSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentAdminViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Instructor.objects.all()
    serializer_class = DepartmentInstructorSerializer

    def destroy(self, request, *args, **kwargs):
        department_id = kwargs.get("pk")
        department = get_object_or_404(Department, pk=department_id)
        department.administrator = None
        department.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    # TODO: do the create by only sending the id
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        department_id = kwargs.get("pk")
        department = get_object_or_404(Department, pk=department_id)
        try:
            admin = department.administrator
        except Instructor.DoesNotExist:
            raise NotFound()

        serializer = DepartmentInstructorSerializer(admin)
        return Response(serializer.data)
