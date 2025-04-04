# Generated by Django 5.1.4 on 2025-03-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0036_alter_series_age_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloadfile',
            name='file_format',
            field=models.CharField(choices=[('MP4', 'MP4'), ('FLV', 'FLV'), ('MOV', 'MOV'), ('MKV', 'MKV'), ('LXF', 'LXF'), ('MXF', 'MXF'), ('AVI', 'AVI'), ('QuickTime', 'QuickTime'), ('WebM', 'WebM')], default='MKV', help_text='File container format.', max_length=20),
        ),
    ]
