from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blog_post/', default='blog_post/default_image_blog.jpg')
    content = models.TextField()
    # category
    # tag
    # status
    # counted_views
    # likes
    # login require
    published_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
