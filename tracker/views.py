from django.shortcuts import render
from .models import Income, Expense
from .forms import ExpenseForm
from django.shortcuts import render, redirect
from .forms import IncomeForm
from django.shortcuts import get_object_or_404

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
def update_income(request, income_id):
    income = get_object_or_404(Income, pk=income_id)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('tracker:income_list')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'tracker/add_income.html', {'form': form})

def delete_income(request, id):
    income = get_object_or_404(Income, pk=income_id)
    if request.method == 'POST':
        income.delete()
        return redirect('tracker:income_list')
    return render(request, 'tracker/confirm_delete.html', {'item': income, 'type': 'Income'})

def update_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('tracker:expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'tracker/add_expense.html', {'form': form})

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    if request.method == 'POST':
        expense.delete()
        return redirect('tracker:expense_list')
    return render(request, 'tracker/confirm_delete.html', {'item': expense, 'type': 'Expense'})
