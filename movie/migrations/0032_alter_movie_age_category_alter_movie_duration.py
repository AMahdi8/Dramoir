# Generated by Django 5.1.4 on 2025-03-03 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0031_alter_crew_country_alter_downloadfile_episode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='age_category',
            field=models.CharField(blank=True, choices=[('G', 'General Audiences(G)'), ('PG', 'Parental Guidance Suggested(PG)'), ('PG-13', 'Parents Strongly Cautioned(PG-13)'), ('R', 'Restricted(R)'), ('NC-17', 'Adults Only(NC-17)')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
