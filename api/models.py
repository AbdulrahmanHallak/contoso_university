from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Instructor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    hire_date = models.DateField()


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    start_date = models.DateField()

    # relations
    administrator = models.ForeignKey(
        Instructor,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="department",
    )


class Course(models.Model):
    title = models.CharField(max_length=50)
    credits = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    # relations
    department = models.ForeignKey(
        Department, on_delete=models.RESTRICT, related_name="department"
    )
    instructors = models.ManyToManyField(Instructor, related_name="courses")


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    enrollment_date = models.DateField()


class Enrollment(models.Model):
    GRADE_CHOICES = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("F", "F"),
    ]
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)

    # relations
    course = models.ForeignKey(
        Course, on_delete=models.RESTRICT, related_name="enrollments"
    )
    student = models.ForeignKey(
        Student, on_delete=models.RESTRICT, related_name="enrollments"
    )


class OfficeAssignment(models.Model):
    instructor = models.OneToOneField(
        Instructor, on_delete=models.CASCADE, primary_key=True
    )
    location = models.CharField(max_length=150)
