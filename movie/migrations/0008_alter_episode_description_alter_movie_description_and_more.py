# Generated by Django 5.1.4 on 2024-12-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_alter_movie_countries_alter_movie_genres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subtitle',
            name='title',
            field=models.CharField(blank=True, null=True),
        ),
    ]
