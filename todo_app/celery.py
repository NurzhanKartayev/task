import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_app.settings')


celery_app = Celery('core')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'todo_deadline': {
        'task': 'todo.deadline_send_mail',
        'schedule': 3600.00
    }
}
