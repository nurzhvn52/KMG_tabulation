# Generated by Django 5.0.3 on 2024-04-23 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0006_alter_timetracking_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='timetracking',
            unique_together=set(),
        ),
    ]