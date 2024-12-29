from rest_framework import serializers

from api.models import Instructor, OfficeAssignment


class OfficeAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeAssignment
        fields = ["location"]


class InstructorSerializer(serializers.ModelSerializer):
    office_assignment = OfficeAssignmentSerializer(read_only=True, source="office")

    class Meta:
        model = Instructor
        fields = "__all__"
