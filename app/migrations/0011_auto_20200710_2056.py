# Generated by Django 3.0.6 on 2020-07-10 14:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_story_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='image',
        ),
        migrations.AddField(
            model_name='story',
            name='time_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
