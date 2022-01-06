from django import forms
from .models import Income,Expense
from django.forms import ModelForm,NumberInput,Select,DateInput
# import django.forms
from .models import *
import datetime


class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ["amount","date","category"]
        choices = CATEGORY_INCOME
        widgets = {"amount":NumberInput(attrs={'class':"form-control",'placeholder':'Input amount'}),
        "date":DateInput(attrs={"class":"form-control",'placeholder':'Input date'}),
        "choices":Select(choices= choices, attrs={"class":"form-control",'placeholder':'Select category'})}


class ExpenceForm(ModelForm):
    class Meta:
        model = Expense
        fields = ["amount","date","category"]
        choices = CATEGORY_EXPENCE
        widgets = {"amount":NumberInput(attrs={'class':"form-control",'placeholder':'Input amount'}),
        "date":DateInput(attrs={"class":"form-control",'placeholder':'Input date'}),
        "choices":Select(choices= choices, attrs={"class":"form-control",'placeholder':'Select category'})}

# ---------------------
class GetStatsForPeriod(forms.Form):
    start_date = forms.DateField(widget = forms.SelectDateWidget(years=range(1980,2100)))
    end_date = forms.DateField(widget = forms.SelectDateWidget(years=range(1980,2100)))
