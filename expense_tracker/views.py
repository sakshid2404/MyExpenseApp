from django.utils import timezone
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Expense
from django.db.models import F, Sum


class ExpenseListView(ListView):
    model = Expense
    template_name = "list.html"
    context_object_name = "expenses"
    ordering = ["-created_at"] 
    
    def get_queryset(self):
        today = timezone.now().date()  
        return Expense.objects.filter(created_at__date=today).order_by("-created_at")

    def get_context_data(self, **kwargs) :
        data = super().get_context_data(**kwargs)
        total = self.get_queryset().aggregate(
            total_sum=Sum(F('amount') * F('quantity'))
        )
        data['total'] = total['total_sum']
        return data
     
    

class ExpenseCreateView(CreateView):
    model = Expense
    template_name = "create.html"
    fields = ["category", "name", "amount", "quantity", 'unit','pay_type']
    success_url = reverse_lazy("expense-list")



