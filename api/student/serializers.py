from rest_framework import serializers

from ..models import Student, Course


class StudentCoursesSerializer(serializers.ModelSerializer):
    # students = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ["id", "title", "credits"]

    # def get_students(self, obj):
    #     return obj.enrollments.count()


class StudentDetailsSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = "__all__"

    def get_courses(self, obj):
        enrollments = obj.enrollments.all()
        courses = [enrollment.course for enrollment in enrollments]
        return StudentCoursesSerializer(courses, many=True).data


class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = "__all__"

    def get_courses(self, obj):
        return obj.enrollments.count()
