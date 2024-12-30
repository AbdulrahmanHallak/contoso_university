from django.shortcuts import get_object_or_404
from rest_framework import viewsets, decorators, status
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import (
    EnrollmentSerializer,
    StudentCoursesSerializer,
    StudentSerializer,
    StudentDetailsSerializer,
)
from api.models import Course, Enrollment, Student


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StudentDetailsSerializer(instance)
        return Response(serializer.data)


@decorators.api_view(["DELETE"])
def delete_student_enrollment(
    request: Request, student_pk=None, course_pk=None, *args, **kwargs
):
    if not (student_pk and course_pk):
        return

    enrollment = get_object_or_404(
        Enrollment, course_id=course_pk, student_id=student_pk
    )
    enrollment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@decorators.api_view(["POST"])
def create_student_enrollment(request: Request, student_pk=None, *args, **kwargs):
    if not student_pk:
        return

    course_pk = request.data.pop("id")  # type: ignore
    student = get_object_or_404(Student, pk=student_pk)
    course = get_object_or_404(Course, pk=course_pk)
    instance = Enrollment(course=course, student=student).save()
    serializer = EnrollmentSerializer(instance)
    return Response(serializer.data, status.HTTP_201_CREATED)
