# Generated by Django 3.0.6 on 2020-07-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='imgfile',
        ),
        migrations.AddField(
            model_name='image',
            name='img',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
    ]