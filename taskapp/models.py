from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField('タスク名', max_length=50)
    text = models.TextField('詳細')
    deadline = models.DateTimeField('期日', default=timezone.datetime.today())
    staff = models.CharField('担当者', max_length=30)
    date = models.DateTimeField('作成日', default=timezone.datetime.today())

    def __str__(self):
        return self.title
