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

class Contact(models.Model):
    first_name = models.CharField(max_length=30)  # first name of contact
    last_name = models.CharField(max_length=30)  # last name of contact
    email = models.EmailField()  # email of contact
    message = models.TextField()  # message of text
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp when contact was created
    updated_at = models.DateTimeField(auto_now=True)  # timestamp when contact was last updated

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'