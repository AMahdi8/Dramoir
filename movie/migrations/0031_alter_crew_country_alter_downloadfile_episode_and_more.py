# Generated by Django 5.1.4 on 2025-02-14 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0030_remove_movie_choosen_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crew',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actors', to='movie.country'),
        ),
        migrations.AlterField(
            model_name='downloadfile',
            name='episode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='download_urls', to='movie.episode'),
        ),
        migrations.AlterField(
            model_name='downloadfile',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='download_urls', to='movie.movie'),
        ),
    ]
