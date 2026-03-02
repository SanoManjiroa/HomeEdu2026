from django.db import models
from django.contrib.auth.models import User as DjangoUser

ROLE_CHOICES = (
    ("ota-ona", "Ota-ona"),
    ("student", "Student")
)

class User(models.Model):
    django_user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    birth_date = models.DateField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    grade = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.django_user.username
