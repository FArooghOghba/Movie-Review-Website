# Generated by Django 3.2.14 on 2022-07-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
