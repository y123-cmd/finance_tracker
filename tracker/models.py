from django.db import models

class Income(models.Model):
    source = models.CharField(max_length=100)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.source} - {self.amount}"

class Expense(models.Model):
    category = models.CharField(max_length=100)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"

