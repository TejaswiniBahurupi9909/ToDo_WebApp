# Generated by Django 3.0.4 on 2020-04-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Enter Your Task'),
        ),
    ]
