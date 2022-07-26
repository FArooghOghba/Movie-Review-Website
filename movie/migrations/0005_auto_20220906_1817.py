# Generated by Django 3.2.14 on 2022-09-06 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20220819_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='CastCrew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(default='cast_crew_image/blank-profile-picture.png', upload_to='cast_crew_image/')),
                ('career', models.CharField(choices=[('Actor', 'Actor'), ('Actress', 'Actress'), ('Director', 'Director'), ('Writer', 'Writer'), ('Producer', 'Producer'), ('Music', 'Music')], default='Actor', max_length=10)),
                ('cast', models.BooleanField(default=False)),
                ('crew', models.BooleanField(default=False)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=64)),
                ('cast_crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.castcrew')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='cast_crew',
            field=models.ManyToManyField(related_name='cast_crew', through='movie.Role', to='movie.CastCrew'),
        ),
    ]
