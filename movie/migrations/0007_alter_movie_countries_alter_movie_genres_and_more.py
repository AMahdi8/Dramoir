# Generated by Django 5.1.4 on 2024-12-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_remove_movie_actors_remove_series_actors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='countries',
            field=models.ManyToManyField(blank=True, related_name='movies', to='movie.country'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, related_name='movies', to='movie.genre'),
        ),
        migrations.AlterField(
            model_name='series',
            name='countries',
            field=models.ManyToManyField(blank=True, related_name='series', to='movie.country'),
        ),
        migrations.AlterField(
            model_name='series',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='series', to='movie.genre'),
        ),
        migrations.AlterField(
            model_name='series',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='series', to='movie.language'),
        ),
    ]
