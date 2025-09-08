from django.db import models


class Expense(models.Model):

    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField() 
    unit = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pay_type =models.CharField(max_length=10)

    @property
    def total(self):
        return self.quantity * self.amount


