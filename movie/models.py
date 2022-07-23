from django.db import models


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=False, unique=True)
    # category
    # tag
    synopsis = models.TextField()
    poster = models.ImageField(upload_to='movie_poster/')
    trailer = models.URLField()
    # cast_crew
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    runtime = models.DurationField()
    votes = models.IntegerField(default=0)
    release_date = models.DateField()
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-release_date']

    def __str__(self):
        return self.title
