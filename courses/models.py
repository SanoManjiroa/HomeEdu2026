from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=160)
    image = models.ImageField(upload_to="course_images/", blank=True, null=True)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at", "title"]

    def __str__(self):
        return self.title

class CourseLesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    video_url = models.URLField(blank=True)
    pdf_file = models.FileField(upload_to="course_pdfs/", blank=True, null=True)
    text = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=1)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["course", "order", "title"]

    def __str__(self):
        return f"{self.course} — {self.title}"
