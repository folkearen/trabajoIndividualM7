# Generated by Django 4.2.4 on 2023-08-28 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_rename_prioridad_priority_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_priority',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='task.priority'),
        ),
    ]