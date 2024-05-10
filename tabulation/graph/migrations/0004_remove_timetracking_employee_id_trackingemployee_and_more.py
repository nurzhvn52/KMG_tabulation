# Generated by Django 5.0.3 on 2024-04-22 04:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0003_remove_timetracking_employees_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetracking',
            name='employee_id',
        ),
        migrations.CreateModel(
            name='TrackingEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph.employees')),
                ('tracking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph.timetracking')),
            ],
        ),
        migrations.AddField(
            model_name='employees',
            name='tracking',
            field=models.ManyToManyField(related_name='tracking_employee', through='graph.TrackingEmployee', to='graph.timetracking'),
        ),
    ]