from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.course_list, name="list"),
    path("<int:course_id>/", views.course_detail, name="detail"),
    path("dars/<int:lesson_id>/", views.lesson_detail, name="lesson_detail"),
]
