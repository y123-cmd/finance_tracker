from django.shortcuts import render
from .models import Income, Expense

def income_list(request):
    incomes = Income.objects.all()  
    return render(request, 'tracker/income_list.html', {'incomes': incomes})

def expense_list(request):
    expenses = Expense.objects.all()  
    return render(request, 'tracker/expense_list.html', {'expenses': expenses})

