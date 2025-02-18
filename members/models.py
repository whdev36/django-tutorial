from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.username
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username