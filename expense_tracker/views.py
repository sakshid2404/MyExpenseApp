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
        queryset = super().get_queryset()
        date = self.request.GET.get("date")
        category = self.request.GET.get("category")
        if date:  
            queryset = queryset.filter(created_at__date=date)
        if category:  
            queryset = queryset.filter(category=category)
        return queryset
    
    
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
    fields = "__all__"
    success_url = reverse_lazy("expense-list")



