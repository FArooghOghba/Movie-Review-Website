# Generated by Django 3.2.14 on 2022-07-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('synopsis', models.TextField()),
                ('poster', models.ImageField(upload_to='movie_poster/')),
                ('trailer', models.URLField()),
                ('rating', models.IntegerField(default=0)),
                ('runtime', models.DurationField()),
                ('votes', models.IntegerField(default=0)),
                ('release_date', models.DateField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-release_date'],
            },
        ),
    ]