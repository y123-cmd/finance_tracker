from django.shortcuts import render
from .models import Income, Expense

def income_list(request):
    incomes = Income.objects.all()  
    return render(request, 'tracker/income_list.html', {'incomes': incomes})

def expense_list(request):
    expenses = Expense.objects.all()  
    return render(request, 'tracker/expense_list.html', {'expenses': expenses})

def home(request):
    return render(request, 'base.html')

def add_income(request):
    return render(request, 'tracker/add_income.html')

def add_expense(request):
    return render(request, 'tracker/add_expense.html')
