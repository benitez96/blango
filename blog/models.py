from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='posts')

    def __str__(self):
        return self.title


class Tag(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value
