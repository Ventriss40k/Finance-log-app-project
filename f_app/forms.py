from .models import Income,Expense
from django.forms import ModelForm,NumberInput,Select,DateInput
from .models import CATEGORY_EXPENCE,CATEGORY_INCOME

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
