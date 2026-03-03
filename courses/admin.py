from django.contrib import admin
from .models import Course, CourseLesson

class CourseLessonInline(admin.TabularInline):
    model = CourseLesson
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at")
    list_filter = ("is_published",)
    search_fields = ("title",)
    inlines = [CourseLessonInline]

@admin.register(CourseLesson)
class CourseLessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order", "is_published")
    list_filter = ("course", "is_published")
    search_fields = ("title", "course__title")
