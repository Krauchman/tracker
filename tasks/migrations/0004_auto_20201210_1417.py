# Generated by Django 3.1.4 on 2020-12-10 08:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_auto_20201210_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='watchers',
            field=models.ManyToManyField(blank=True, related_name='watched_tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]