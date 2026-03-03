from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=180)
    location = models.CharField(max_length=180, blank=True)
    description = models.TextField()
    salary_text = models.CharField(max_length=120, blank=True)
    skills_text = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
