from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    author_ln = models.CharField('Фамилия', max_length=50)
    author_fn = models.CharField('Имя', max_length=50)

    def __str__(self):
        return self.title
