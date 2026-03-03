from django.urls import path
from . import views

app_name = "education"

urlpatterns = [
    path("", views.grades_list, name="grades"),
    path("<int:grade_id>/", views.subjects_by_grade, name="subjects_by_grade"),
    path("subject/<int:subject_id>/", views.topics_by_subject, name="topics_by_subject"),
    path("topic/<int:topic_id>/", views.topic_detail, name="topic_detail"),
]
