from rest_framework import serializers

from api.models import Enrollment, Student, Course


class StudentCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "credits"]


class StudentDetailsSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()

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


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
