import calendar
from django.shortcuts import render
from .models import *
from tabel.models import Tabel
from .forms import *
# Create your views here.

month_names_ru = {
    "January": "Январь",
    "February": "Февраль",
    "March": "Март",
    "April": "Апрель",
    "May": "Май",
    "June": "Июнь",
    "July": "Июль",
    "August": "Август",
    "September": "Сентябрь",
    "October": "Октябрь",
    "November": "Ноябрь",
    "December": "Декабрь"
}

#filter checking valid or not
def is_valid_queryparam(param):
    return param != '---' and param is not None



def home(request):
    graph =  Graph.objects.all()
    reservoir_form = GraphReservoirForm()
    subdivision_form = GraphSubdivisionForm()
    years = YearSelectForm()

    #filters start

    filter_year = request.GET.get('years')
    request.session['selected_year'] = filter_year

    filter_reservoir = request.GET.get('mesto')
    request.session['selected_reservoir'] = filter_reservoir

    filter_subdiv = request.GET.get('podrazd')
    request.session['selected_subdivision'] = filter_subdiv


    if is_valid_queryparam(filter_year):
        graph = graph.filter(year=filter_year)

    if is_valid_queryparam(filter_reservoir):
        graph = graph.filter(reservoir__name__icontains=filter_reservoir)

    if is_valid_queryparam(filter_subdiv):
        graph = graph.filter(subdivision__name__icontains=filter_subdiv)

    #filters end
        
    context = {
        'selected_year':request.session['selected_year'],
        "selected_reservoir": request.session['selected_reservoir'],
        "selected_subdivision": request.session['selected_subdivision'],        
        'graph':graph,
        'year_form':years,
        "reservoir":reservoir_form,
        "subdivision":subdivision_form,
    }
    return render(request,'graph/home.html',context)



def graph_admin(request):
    #chosen graph
    if 'graph_pk' in request.GET:
        graph_pk = request.GET['graph_pk']
        request.session['chosen_pk'] = graph_pk
        
    #soglasovat' graphik
    if request.method == 'POST':
        # Check if the submitted form contains the key 'soglasovat'
        if 'soglasovat' in request.POST:
            print('log')
            graph_pk = request.POST.get('graph_pk')
            graph_inst = Graph.objects.get(pk=graph_pk)
            # Create a Tabel instance with data from the chosen graph
            employees_graph = graph.employees.all()
            if not Tabel.objects.filter(
                reservoir=graph_inst.reservoir,
                subdivision=graph_inst.subdivision,
                month=graph_inst.month,
                year=graph_inst.year,
                employees=employees_graph
            ).exists():
                # If Tabel object doesn't exist, create it
                Tabel.objects.create(
                    reservoir=graph_inst.reservoir,
                    subdivision=graph_inst.subdivision,
                    month=graph_inst.month,
                    year=graph_inst.year,
                    employees=employees_graph
                )
                print('ne bilo, no sozdal')
            print('poluchilos')
        print('ne poluchilos')


    graph_pk = request.session['chosen_pk']  
    graph = Graph.objects.get(pk=graph_pk)
    employees = graph.employees.all()
    for employee in employees:
        print(employee.name)
    attendance = Attendance.objects.filter(type='дни явок')
    no_attendance = Attendance.objects.filter(type='дни неявок')
    tracking = TimeTracking.objects.all()
    month = graph.month
    year = graph.year


    name_month_en = calendar.month_name[int(month)]
    name_month_ru = month_names_ru[name_month_en]

    if month and month is not None:
        filter_month = int(month)
        tracking = TimeTracking.objects.filter(employee_id__in = employees.values_list('tabel_number',flat=True))
        tracking = tracking.filter(date__month=filter_month)
        tabel_numbers = tracking.values_list('employee_id',flat=True)
        employees = employees.filter(tabel_number__in=tabel_numbers)
    if year and year is not None:
        filter_year = int(year)
        tracking = TimeTracking.objects.filter(employee_id__in = employees.values_list('tabel_number',flat=True))
        tracking = tracking.filter(date__year=filter_year)
        tabel_numbers = tracking.values_list('employee_id',flat=True)
        employees = employees.filter(tabel_number__in=tabel_numbers)

    dates = tracking.values_list('date',flat=True).distinct()
    for date in dates:
        month = date.month
        year = date.year
    
    num_days = calendar.monthrange(int(year),int(month))[1]
    days = range(1,num_days+1)

    #calculation attendace start
    directory = {}
    for employee in employees:
        pairs = [('worked_days', 0), ('weekends', 0), ('days_in_month', len(days)), ('total_work_hours', 0)]
        directory[f'{employee.name}'] = dict(pairs)

    for employee in employees:
        for work in tracking:
            if work.employee_id == employee:
                if str(work.worked_hours).isdigit():
                    directory[f'{employee.name}']['worked_days'] += 1 
                    directory[f'{employee.name}']['total_work_hours'] += int(work.worked_hours)
                else:
                    directory[f'{employee.name}']['weekends'] += 1

    #calculation attendace end

    context = {
        'graph_pk':graph_pk,
        "year":year,
        "month":month,
        'days':days,
        "selected_month": name_month_ru,
        'employees':employees,
        'attendance': attendance, 
        'no_attendance': no_attendance,
        'time_tracking': tracking,
        'graph':graph,
        'calculations': directory,
    }
    return render(request,'graph/graph_admin.html',context)

