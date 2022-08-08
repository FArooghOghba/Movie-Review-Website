from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

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
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='blog_post/', default='blog_post/default_image_blog.jpg')
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    like = models.ManyToManyField(User, blank=True, related_name='collected_likes')
    tag = TaggableManager()
    # login require
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def total_like(self):
        return self.like.count()

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'post_slug': self.slug})

    def get_comments(self):
        return self.comments.filter(parent=None, approved=True)

    def total_comment(self):
        return self.comments.filter(parent=None, approved=True).count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    approved = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def get_reply_comments(self):
        return Comment.objects.filter(parent=self, approved=True)

    def __str__(self):
        return f'{self.content}'
