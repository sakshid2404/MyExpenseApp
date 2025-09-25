from django.contrib import admin
from .models import Expense, Budget


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount','quantity','category', 'name','unit', 'created_at')
    
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['category', 'budget_amount', 'start_date', 'end_date', 'created_at']


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Budget, BudgetAdmin)