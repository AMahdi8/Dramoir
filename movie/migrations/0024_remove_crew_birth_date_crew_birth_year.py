# Generated by Django 5.1.4 on 2025-01-22 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0023_alter_movie_release_year_alter_season_release_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crew',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='crew',
            name='birth_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
