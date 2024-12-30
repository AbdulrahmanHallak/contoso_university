from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

department_router = DefaultRouter()
department_router.register(viewset=views.DepartmentViewSet, prefix="")

admin_router = DefaultRouter()
admin_router.register("", views.DepartmentAdminViewSet)
# TODO: why are the routers for admin not working

print(admin_router.urls)
urlpatterns = [
    path("", include(department_router.urls)),
    # ? this works
    path(
        "<int:pk>/administrator/",
        views.DepartmentAdminViewSet.as_view(
            {"get": "retrieve", "post": "create", "delete": "destroy"}
        ),
    ),
    # ? this does not
    # path("<int:pk>/administrator", include(admin_router.urls)),
    path("<int:department_pk>/course/", include("api.department.course.urls")),
]
