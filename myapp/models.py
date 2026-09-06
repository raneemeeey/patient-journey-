
from django.db import models


class Surgery(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    specialty = models.CharField(max_length=100)
    subspecialty = models.CharField(max_length=100)

    short_description = models.TextField()

    image_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
