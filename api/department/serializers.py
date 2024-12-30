from rest_framework import serializers

from api.models import Department, Instructor


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    administrator = InstructorSerializer(read_only=True)

    class Meta:
        model = Department
        fields = "__all__"
