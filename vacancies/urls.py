from django.urls import path
from . import views

app_name = "vacancies"

urlpatterns = [
    path("", views.vacancy_list, name="list"),
    path("<int:vacancy_id>/", views.vacancy_detail, name="detail"),
]
