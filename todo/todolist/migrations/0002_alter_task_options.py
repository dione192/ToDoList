# Generated by Django 4.2 on 2023-04-05 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задание', 'verbose_name_plural': 'Задания'},
        ),
    ]
