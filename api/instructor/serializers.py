from rest_framework import serializers

from api.models import Course, Instructor, OfficeAssignment


class OfficeAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeAssignment
        fields = ["instructor_id", "location"]


class InstructorSerializer(serializers.ModelSerializer):
    office_assignment = OfficeAssignmentSerializer(read_only=True, source="office")

    class Meta:
        model = Instructor
        fields = "__all__"


class InstructorCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "credits"]
