# Generated by Django 3.1.4 on 2020-12-10 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20201210_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completion_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='expected_completion_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
