from django.contrib import admin
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount','quantity','category', 'name','unit', 'created_at')

admin.site.register(Expense, ExpenseAdmin)