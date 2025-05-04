from django.db import models
from django.utils.text import slugify


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            i = 1
            while Organization.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{i}"
                i += 1
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
