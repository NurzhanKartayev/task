from datetime import datetime, timedelta

from django.core.mail import send_mail

from todo.models import Assignment
from todo_app.celery import celery_app


@celery_app.task(
    name='todo.deadline_send_mail'
)
def deadline_send_mail():
    try:
        assignments = Assignment.objects.filter(deadline__lte=datetime.now() + timedelta(minutes=60))
        for assignment in assignments:
            send_mail("Напоминание о дедлайне", "Дедлайн задачи: " + str(assignment.title) + " закончится через час",
                      "nurzhan.kartaev@mail.ru", [assignment.employee.user.email, ])
    except Exception as exc:
        return {'error': f" Can't send a message ({exc})"}
