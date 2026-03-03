from django.urls import path
from . import views

app_name = "parents"

urlpatterns = [
    path("", views.parent_list, name="list"),
    path("<int:item_id>/", views.parent_detail, name="detail"),
]
