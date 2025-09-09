from django.db import models


class Expense(models.Model):
    
    CATEGORY_CHOICES = [
        ("household", "Household"),
        ("food", "Food & Groceries"),
        ("transport", "Transportation"),
        ("health", "Health & Personal Care"),
        ("education", "Education"),
        ("entertainment", "Entertainment"),
        ("shopping", "Shopping"),
        ("financial", "Financial"), 
    ]
    
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    quantity = models.IntegerField() 
    unit = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pay_type =models.CharField(max_length=10)

    @property
    def total(self):
        return self.quantity * self.amount


