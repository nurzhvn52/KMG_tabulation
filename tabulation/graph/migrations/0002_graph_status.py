# Generated by Django 5.0.3 on 2024-05-15 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='status',
            field=models.CharField(choices=[('согласованный', 'Согласованный'), ('не согласованный', 'Не согласованный')], default='Не согласованный', max_length=20),
        ),
    ]