# Generated by Django 5.1.4 on 2025-03-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0032_alter_movie_age_category_alter_movie_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='series',
            name='trend',
            field=models.BooleanField(default=False),
        ),
    ]
