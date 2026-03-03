from django.contrib import admin
from .models import ParentContent

@admin.register(ParentContent)
class ParentContentAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at")
    list_filter = ("is_published",)
    search_fields = ("title",)
