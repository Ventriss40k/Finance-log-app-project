from django.db.models.aggregates import Avg,Sum
from django.shortcuts import render, redirect
# from django.db.models import Sum
from .models import Income
from .models import Expense
from .forms import IncomeForm,ExpenceForm,GetStatsForPeriod
import calendar
from datetime import date, datetime

# def index(request): # request is must have parameter even if not used in function
#     return HttpResponse("<h4>Welcome to finance app<h4>") # HttpResponce - prints text (not a site page)
# # <h4> is a html tag (header 4) - html tags can be used or no, bu desire. This makes a header of string

def index(request):
    current_month_start = date.today().replace(day=1)
    current_mounth = datetime.now().month
    current_year = datetime.now().year
    current_month_end = calendar.monthrange(current_year,current_mounth)[1]
    start_end_current_month = [f"{current_month_start}",f"{current_year}-{current_mounth}-{current_month_end}"]
    

    # current_balance = 
    incomes = Income.objects.all().filter(date__range = start_end_current_month)
    sum_expences = Expense.objects.all().aggregate(sum = Sum('amount')).get('sum')
    sum_incomes = Income.objects.all().aggregate(sum = Sum('amount')).get('sum')
    total_balance = sum_incomes-sum_expences
    if total_balance == None:
        total_balance = 0
    current_months_sum_incomes = Income.objects.all().filter(date__range =start_end_current_month ).aggregate(sum = Sum('amount')).get('sum')
    if current_months_sum_incomes ==None: 
        current_months_sum_incomes = 0
    current_months_sum_expenses = Expense.objects.all().filter(date__range =start_end_current_month ).aggregate(sum = Sum('amount')).get('sum')
    if current_months_sum_expenses == None:
        current_months_sum_expenses = 0
    # Incomes_mounth = incomes.values('amount').order_by('amount')
    return render(request,'f_app/index.html', {'title': 'Main site page', 'incomes': incomes, 'total_balance': total_balance,'current_months_sum_incomes':current_months_sum_incomes, 'current_months_sum_expenses': current_months_sum_expenses })
    # 1st arg is request (must have), second - html template. Path is listed as if you already in 'templates' folder, third - arguments for html template use

def stats_for_period(request):
    if request.method == 'POST':
        form = GetStatsForPeriod(request.POST)
        if form.is_valid():
            print(form.cleaned_data['start_date'])
            period_start = form.cleaned_data['start_date']
            period_end = form.cleaned_data['end_date']
            period = [period_start,period_end]
            result_incomes = Income.objects.all().filter(date__range =period ).aggregate(sum = Sum('amount')).get('sum')
            if result_incomes == None:
                result_incomes = 0
            result_expences = Expense.objects.all().filter(date__range =period ).aggregate(sum = Sum('amount')).get('sum')
            if result_expences == None:
                result_expences = 0
            
            result_balance = result_incomes - result_expences
            return render(request,'f_app/stats_for_period.html',{'title':'Stats for period','form': form, 'result_title': f" For period {period_start} to {period_end}", 
            'result_incomes':f"Incomes: {result_incomes} UAH",'result_expences': f'Expences: {result_expences} UAH','result_balance':f'Balance: {result_balance} UAH' })

    form = GetStatsForPeriod()
    return render(request,'f_app/stats_for_period.html',{'title':'Stats for period','form': form, 'result_title':'','result_incomes':'','result_expences':'','result_balance':''})




def new_income(request):
    error = ''
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error ='Form is invalid'
    form = IncomeForm()
    context ={'form':form, 'error': error}
    return render(request, 'f_app/new_income.html',context)

def new_expence(request):
    error = ''
    if request.method == 'POST':
        form = ExpenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error ='Form is invalid'
    form = ExpenceForm()
    context ={'form':form, 'error': error}
    return render(request, 'f_app/new_expence.html',context)

# def about(request):
#     return HttpResponse("<h2>This is about section<h2>\n<h6>Here is information about app<h6>")


def about(request):
    return render(request,'f_app/about.html')

# Добавление расхода


# Добавление дохода