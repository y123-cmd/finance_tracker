from django.shortcuts import render
from .models import Income, Expense
from .forms import ExpenseForm
from django.shortcuts import render, redirect
from .forms import IncomeForm

def income_list(request):
    incomes = Income.objects.all()  
    return render(request, 'tracker/income_list.html', {'incomes': incomes})

def expense_list(request):
    expenses = Expense.objects.all()  
    return render(request, 'tracker/expense_list.html', {'expenses': expenses})

def home(request):
    return render(request, 'base.html')

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('tracker:income_list')  
    else:
        form = IncomeForm()

    return render(request, 'tracker/add_income.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':  
        form = ExpenseForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('tracker:expense_list')  
    else:
        form = ExpenseForm()  
    
    return render(request, 'tracker/add_expense.html', {'form': form})
