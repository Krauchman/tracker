from django.db import models

from django.contrib.auth.models import User


STATUS_CHOICES = (
    'Planning',
    'Active',
    'Control',
    'Completed',
)


class Status(models.IntegerChoices):
    PLANNING = 0, 'Planning'
    ACTIVE = 1, 'Active'
    CONTROL = 2, 'Control'
    COMPLETED = 3, 'Completed'


class Task(models.Model):

    name = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=True)

    status = models.IntegerField(choices=Status.choices, default=Status.PLANNING)

    start_time = models.DateTimeField(null=True)
    completion_time = models.DateTimeField(null=True)
    expected_completion_time = models.DateTimeField(null=True)

    performer = models.ForeignKey(User, related_name='tasks', null=True, on_delete=models.SET_NULL)
    watchers = models.ManyToManyField(User, related_name='watched_tasks', blank=True)


class StatusChange(models.Model):
    old = models.IntegerField(choices=Status.choices)
    new = models.IntegerField(choices=Status.choices)

    task = models.ForeignKey(Task, related_name='status_changes', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='status_changes', null=True, on_delete=models.SET_NULL)
