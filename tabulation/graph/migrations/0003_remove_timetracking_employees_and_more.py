# Generated by Django 5.0.3 on 2024-04-22 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0002_trackingemployee_timetracking_employees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetracking',
            name='employees',
        ),
        migrations.DeleteModel(
            name='TrackingEmployee',
        ),
    ]