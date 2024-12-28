import random
from faker import Faker
from django.db import transaction
from api.models import (
    Instructor,
    Department,
    Course,
    Student,
    Enrollment,
    OfficeAssignment,
)

fake = Faker()


@transaction.atomic
def generate_instructors(n=10):
    instructors = []
    for _ in range(n):
        instructors.append(
            Instructor(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                hire_date=fake.date_between(start_date="-10y", end_date="today"),
            )
        )
    Instructor.objects.bulk_create(instructors)
    print(f"Created {n} instructors.")


def generate_departments(n=5):
    # Predefined list of university majors for more realistic names
    majors = [
        "Computer Science",
        "Mathematics",
        "Physics",
        "Biology",
        "Chemistry",
        "Engineering",
        "Psychology",
        "Economics",
        "History",
        "Philosophy",
        "Literature",
        "Sociology",
        "Political Science",
        "Art History",
        "Education",
    ]

    instructors = list(Instructor.objects.all())
    departments = []

    for _ in range(n):
        name = random.choice(majors)  # Pick a random major
        majors.remove(name)  # Ensure no duplicates

        departments.append(
            Department(
                name=name,
                budget=fake.pydecimal(left_digits=7, right_digits=2, positive=True),
                start_date=fake.date_between(start_date="-10y", end_date="today"),
                administrator=random.choice(instructors) if instructors else None,
            )
        )

    Department.objects.bulk_create(departments)
    print(f"Created {n} departments.")


def generate_courses(n=20):
    departments = list(Department.objects.all())
    courses = []
    for _ in range(n):
        courses.append(
            Course(
                title=fake.sentence(nb_words=3).rstrip("."),
                credits=random.randint(1, 5),
                department=random.choice(departments) if departments else None,
            )
        )
    Course.objects.bulk_create(courses)
    print(f"Created {n} courses.")


def assign_course_instructors():
    instructors = list(Instructor.objects.all())
    courses = Course.objects.all()
    for course in courses:
        course.instructors.set(random.sample(instructors, k=random.randint(1, 3)))
    print("Assigned instructors to courses.")


def generate_students(n=50):
    students = []
    for _ in range(n):
        students.append(
            Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                enrollment_date=fake.date_between(start_date="-4y", end_date="today"),
            )
        )
    Student.objects.bulk_create(students)
    print(f"Created {n} students.")


def generate_enrollments():
    students = list(Student.objects.all())
    courses = list(Course.objects.all())
    enrollments = []
    for _ in range(200):  # Arbitrary number of enrollments
        enrollments.append(
            Enrollment(
                grade=random.choice(["A", "B", "C", "D", "F"]),
                course=random.choice(courses) if courses else None,
                student=random.choice(students) if students else None,
            )
        )
    Enrollment.objects.bulk_create(enrollments)
    print("Created enrollments.")


def generate_office_assignments():
    instructors = Instructor.objects.all()
    for instructor in instructors:
        if random.choice([True, False]):  # Randomly assign office
            OfficeAssignment.objects.create(
                instructor=instructor, location=fake.address()
            )
    print("Created office assignments.")


def generate_fake_data():
    generate_instructors()
    generate_departments()
    generate_courses()
    assign_course_instructors()
    generate_students()
    generate_enrollments()
    generate_office_assignments()


if __name__ == "__main__":
    print("started")
    generate_fake_data()
