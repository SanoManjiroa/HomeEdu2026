from django.contrib import admin
from .models import Vacancy

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "salary_text", "is_active", "created_at")
    list_filter = ("is_active", "location")
    search_fields = ("title", "location", "description", "skills_text")
