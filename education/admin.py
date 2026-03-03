from django.contrib import admin
from .models import Grade, Subject, Topic

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("number",)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "grade", "is_published")
    list_filter = ("grade", "is_published")
    search_fields = ("name",)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "order", "is_published")
    list_filter = ("subject__grade", "subject", "is_published")
    search_fields = ("title", "subject__name")
