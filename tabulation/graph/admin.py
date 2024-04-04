from typing import Any
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.admin.sites import site
from django.http import HttpResponse
from .models import *
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
# Register your models here.

    
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name','description')

@admin.register(Attendance)
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ('type','name','description')

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('tabel_number',
                    'name',
                    'surname',
                    'middlename',
                    'job',
                    'oil_place')

@admin.register(Graph)
class GraphAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'reservoir',
                    'subdivision',
                    'month',
                    'year',
                    'view_graph_link',
                    )
    list_filter = ('reservoir',
                   'year',
                   'subdivision')

    #Add link to check each graph by pk
    def view_graph_link(self,obj):
        graph = obj.pk
        url = (
            reverse("graph:graph_admin")
                    +"?"
                    +urlencode({'graph_pk':graph})
        )
        return format_html('<a href={}>{}',url,f"График Вахты №{graph}")
    view_graph_link.short_description = 'Графики'

@admin.register(OilPlace)
class OilPlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('name',)

# class TimeTrackingEmployeeInline(admin.TabularInline):
#      model = TimeTracking.employee_id.through
#      extra = 1

@admin.register(TimeTracking)
class TimeTrackingAdmin(admin.ModelAdmin):
        list_display = (
                    'employee_id',
                    'worked_hours',
                    'date',
                    )
        
# @admin.register(GraphEmployeesList)
# class GraphEmployeesListAdmin(admin.ModelAdmin):
#     list_display = ('employee_id', 'graph_id')
        




