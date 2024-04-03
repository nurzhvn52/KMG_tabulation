# Generated by Django 4.2.7 on 2024-04-02 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0003_alter_attendance_type'),
        ('tabel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTrackingTabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('worked_hours', models.CharField(default='0', max_length=5, null=True, verbose_name='Проработано часов')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graph.employees', verbose_name='Табельный Номер')),
            ],
            options={
                'verbose_name': 'Контроль времени работников',
                'verbose_name_plural': 'Контроль времени работников',
                'unique_together': {('date', 'employee_id')},
            },
        ),
    ]
