from django.contrib import admin

from .models import (
    Course,
    Department,
    Enrollment,
    Instructor,
    OfficeAssignment,
    Student,
)

# Register your models here.
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Enrollment)
admin.site.register(Instructor)
admin.site.register(OfficeAssignment)
admin.site.register(Student)
