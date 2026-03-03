from django.db import models

class ContactInfo(models.Model):
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    telegram = models.CharField(max_length=120, blank=True)
    address = models.CharField(max_length=250, blank=True)
    map_url = models.URLField(blank=True)

    def __str__(self):
        return "ContactInfo"

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} ({self.created_at:%Y-%m-%d})"
