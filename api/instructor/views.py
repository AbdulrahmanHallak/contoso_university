from rest_framework import viewsets, mixins, generics, decorators, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.models import Course, Instructor, OfficeAssignment
from .serializers import (
    InstructorCoursesSerializer,
    InstructorSerializer,
    OfficeAssignmentSerializer,
)


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class OfficeViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = OfficeAssignment.objects.all()
    serializer_class = OfficeAssignmentSerializer


class InstructorCoursesListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = InstructorCoursesSerializer

    def get_queryset(self):
        instructor_id = self.kwargs.get("pk")
        if instructor_id:
            return super().get_queryset().filter(instructors__pk=instructor_id)
        return super().get_queryset()


@decorators.api_view(["DELETE"])
def delete_instructor_course(
    request, instructor_pk=None, course_pk=None, *args, **kwargs
):
    if not (instructor_pk and course_pk):
        return

    course = get_object_or_404(Course, pk=course_pk)
    instructor = get_object_or_404(Instructor, pk=instructor_pk)
    course.instructors.remove(instructor)
    return Response(status=status.HTTP_204_NO_CONTENT)


@decorators.api_view(["POST"])
def create_instructor_course(request, instructor_pk=None, *args, **kwargs):
    if not instructor_pk:
        return

    course_pk = request.data.pop("id")  # type: ignore
    instructor = get_object_or_404(Instructor, pk=instructor_pk)
    course = get_object_or_404(Course, pk=course_pk)
    course.instructors.add(instructor)
    return Response(status.HTTP_201_CREATED)
