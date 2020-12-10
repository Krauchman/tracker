from celery import shared_task
from django.core.mail import send_mail

from tasks.models import Task, STATUS_CHOICES


@shared_task
def notify_status_change(task_pk, receivers):
    task = Task.objects.get(pk=task_pk)

    subject = 'Status change'
    message = 'Hello,\n\nThe status of a task {} has changed to {}'.format(
        task.name,
        STATUS_CHOICES[task.status],
    )
    sender = 'testmail@mail.com'

    send_mail(subject, message, sender, receivers, fail_silently=False)
