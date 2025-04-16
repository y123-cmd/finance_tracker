
from django.urls import path
from . import views

app_name = "tracker"


urlpatterns = [
    path('', views.home, name='home'),
    path('income/', views.income_list, name='income_list'),
    path("income/add/", views.add_income, name="add_income"),
    path('income/update/<int:income_id>/', views.update_income, name='update_income'),
    path('income/delete/<int:id>/', views.delete_income, name='delete_income'),

    path('expense/', views.expense_list, name='expense_list'),
    path("expenses/add/", views.add_expense, name="add_expense"),
    path('expense/update/<int:expense_id>/', views.update_expense, name='update_expense'),
    path('expense/delete/<int:id>/', views.delete_expense, name='delete_expense'),
]
