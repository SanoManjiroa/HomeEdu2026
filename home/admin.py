from django.contrib import admin
from .models import (
    SchoolGrade, Subject, LessonTopic,
    ParentTraining, VideoLesson,
    CourseCategory, Course,
    Vacancy, Resume, ContactMessage
)


@admin.register(SchoolGrade)
class SchoolGradeAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title",)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("title", "grade", "order", "is_active")
    list_filter = ("grade", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title",)


@admin.register(LessonTopic)
class LessonTopicAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "order", "status")
    list_filter = ("status", "subject__grade")
    search_fields = ("title", "subject__title")


@admin.register(ParentTraining)
class ParentTrainingAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("title",)


@admin.register(VideoLesson)
class VideoLessonAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("title",)


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "order", "is_active")
    list_editable = ("order", "is_active")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "price", "duration_weeks", "created_at")
    list_filter = ("status", "category")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "location", "job_type", "status", "created_at")
    list_filter = ("status", "job_type")
    search_fields = ("title", "company", "description")


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "profession", "phone", "is_public", "created_at")
    list_filter = ("is_public",)
    search_fields = ("full_name", "profession", "skills")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "created_at")
    search_fields = ("name", "phone", "email", "message")