# Generated by Django 5.1.4 on 2025-02-10 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0028_alter_crew_image_alter_movie_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloadfile',
            name='quality',
            field=models.CharField(choices=[('144p', '144p'), ('240p', '240p'), ('360p', '360p'), ('480p', '480p'), ('540p', '540p'), ('720p', '720p'), ('1080p', '1080p'), ('1440p', '1440p'), ('2160p', '2160p'), ('4320p', '4320p')], max_length=20),
        ),
    ]
