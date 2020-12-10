from rest_framework import serializers

from .models import Task, StatusChange


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'status',
            'start_time',
            'completion_time',
            'expected_completion_time',
            'performer',
            'watchers',
        ]
        read_only_fields = ['status']


class StatusChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusChange
        fields = ['old', 'new', 'task', 'author']
        read_only_fields = ['old', 'author']
