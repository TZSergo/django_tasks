# Generated by Django 4.1 on 2022-09-06 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_task_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='author',
        ),
        migrations.AddField(
            model_name='task',
            name='author_fn',
            field=models.CharField(default=1, max_length=50, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='author_ln',
            field=models.CharField(default=1, max_length=50, verbose_name='Фамилия'),
            preserve_default=False,
        ),
    ]
