from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()  # ⬅️ use this instead of TextField
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

