# Generated by Django 3.0.6 on 2020-07-11 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorview',
            name='content',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Story'),
        ),
    ]
