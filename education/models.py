from django.db import models

class Grade(models.Model):
    number = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.number}-sinf"

class Subject(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="subjects")
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        unique_together = ("grade", "name")
        ordering = ["grade__number", "name"]

    def __str__(self):
        return f"{self.grade}: {self.name}"

class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=200)
    video_url = models.URLField(blank=True, help_text="YouTube embed URL: https://www.youtube.com/embed/VIDEO_ID")
    pdf_file = models.FileField(upload_to="topic_pdfs/", blank=True, null=True)
    text = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=1)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["subject__grade__number", "subject__name", "order", "title"]

    def __str__(self):
        return f"{self.subject} — {self.title}"
