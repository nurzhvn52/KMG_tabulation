from django.db.models.signals import pre_delete,post_delete
from .models import *
from django.dispatch import receiver

@receiver(pre_delete,sender=Graph)
def pre_delete_graph(sender,instance,*args, **kwargs):
    employees_graph = instance.employees.all()
    month = instance.month
    year = instance.year

    # Delete corresponding time tracking entries for each employee
    for employee in employees_graph:
        TimeTracking.objects.filter(employee_id=employee, date__month=month, date__year=year).delete()
    print('timetracking graph deleted!!')