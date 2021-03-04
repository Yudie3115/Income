from django.db import models

# Create your models here.


class Income(models.Model):
    income_date = models.DateField(auto_now=False, auto_now_add=False)
    amount = models.IntegerField()
    source = models.CharField(max_length=50)


class Expenses(models.Model):
    expense_date = models.DateField(auto_now=False, auto_now_add=False)
    expense = models.CharField(max_length=50)
    income = models.ForeignKey(Income, on_delete=models.CASCADE)
    expense_amount = models.IntegerField()
