from typing import Tuple

from django.contrib.auth.models import User
from django.db import models

from django.utils.translation import gettext_lazy as _


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user', related_name='employee')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')


class Assignment(models.Model):
    LOW: str = 'low'
    MEDIUM: str = 'medium'
    HIGH: str = 'high'

    PRIORITY_TYPES: Tuple = (
        (LOW, LOW), (MEDIUM, MEDIUM), (HIGH, HIGH)
    )

    title = models.CharField(max_length=100, db_index=True, null=False)
    description = models.CharField(max_length=256, null=False)
    priority = models.CharField(choices=PRIORITY_TYPES, max_length=50)
    deadline = models.DateTimeField(verbose_name='deadline')
    employee = models.ForeignKey(Employee, related_name='assignments',
                                 on_delete=models.CASCADE, verbose_name=_('employee'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('assignment')
        verbose_name_plural = _('assignments')


