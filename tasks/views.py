from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .models import Task, StatusChange
from .serializers import TaskSerializer, StatusChangeSerializer

from tasks.tasks import notify_status_change


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatusChangeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StatusChange.objects.all()
    serializer_class = StatusChangeSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatusChangeCreateAPIView(CreateAPIView):
    serializer_class = StatusChangeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        task = serializer.validated_data['task']
        instance = serializer.save(author=self.request.user, old=task.status)
        task.status = instance.new
        task.save()
        notify_status_change.delay(task.pk, [watcher.email for watcher in task.watchers.all()])
