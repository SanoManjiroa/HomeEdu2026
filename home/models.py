from django.db import models
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PublishedStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"


# -------------------------
# SCHOOL (Maktab)
# -------------------------
class SchoolGrade(TimeStampedModel):
    title = models.CharField(max_length=100)   # "5-sinf"
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title


class Subject(TimeStampedModel):
    title = models.CharField(max_length=120)   # "Matematika"
    grade = models.ForeignKey(SchoolGrade, on_delete=models.CASCADE, related_name="subjects")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["grade__order", "order", "title"]

    def __str__(self):
        return f"{self.grade} — {self.title}"


class LessonTopic(TimeStampedModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=160)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=12, choices=PublishedStatus.choices, default=PublishedStatus.DRAFT)

    class Meta:
        ordering = ["subject__grade__order", "subject__order", "order", "title"]

    def __str__(self):
        return f"{self.subject} — {self.title}"


# -------------------------
# Parents (Ota-onalar)
# -------------------------
class ParentTraining(TimeStampedModel):
    title = models.CharField(max_length=180)
    description = models.TextField()
    cover = models.ImageField(upload_to="trainings/covers/", blank=True, null=True)
    status = models.CharField(max_length=12, choices=PublishedStatus.choices, default=PublishedStatus.DRAFT)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class VideoLesson(TimeStampedModel):
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    youtube_url = models.URLField(blank=True)
    file = models.FileField(upload_to="videos/", blank=True, null=True)
    status = models.CharField(max_length=12, choices=PublishedStatus.choices, default=PublishedStatus.DRAFT)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


# -------------------------
# Courses (Kurslar)
# -------------------------
class CourseCategory(TimeStampedModel):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:140]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Course(TimeStampedModel):
    category = models.ForeignKey(CourseCategory, on_delete=models.PROTECT, related_name="courses")
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    cover = models.ImageField(upload_to="courses/covers/", blank=True, null=True)

    duration_weeks = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)  # so'm
    has_certificate = models.BooleanField(default=True)

    status = models.CharField(max_length=12, choices=PublishedStatus.choices, default=PublishedStatus.DRAFT)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:200]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# -------------------------
# Vacancies (Vakansiya)
# -------------------------
class JobType(models.TextChoices):
    FULL_TIME = "full_time", "Full-time"
    PART_TIME = "part_time", "Part-time"
    REMOTE = "remote", "Remote"
    INTERNSHIP = "internship", "Internship"


class Vacancy(TimeStampedModel):
    title = models.CharField(max_length=180)
    company = models.CharField(max_length=180, blank=True)
    location = models.CharField(max_length=180, blank=True)
    job_type = models.CharField(max_length=20, choices=JobType.choices, default=JobType.FULL_TIME)

    salary_from = models.PositiveIntegerField(blank=True, null=True)
    salary_to = models.PositiveIntegerField(blank=True, null=True)

    description = models.TextField()
    requirements = models.TextField(blank=True)

    status = models.CharField(max_length=12, choices=PublishedStatus.choices, default=PublishedStatus.DRAFT)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


# -------------------------
# Resume & Contact
# -------------------------
class Resume(TimeStampedModel):
    full_name = models.CharField(max_length=160)
    phone = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=160, blank=True)

    profession = models.CharField(max_length=160, blank=True)
    skills = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    portfolio_url = models.URLField(blank=True)
    cv_file = models.FileField(upload_to="resumes/", blank=True, null=True)

    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.full_name


class ContactMessage(TimeStampedModel):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.created_at:%Y-%m-%d})"