from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
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
    categories = models.ManyToManyField(Category)
    like = models.ManyToManyField(User, blank=True, related_name='collected_likes')
    # tag
    # status
    # counted_views
    # login require
    published_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def total_like(self):
        return self.like.count()

    def __str__(self):
        return self.title
