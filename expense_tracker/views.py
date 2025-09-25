from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.db.models import F, Sum
from .models import Expense, Budget


class ExpenseListView(ListView):
    model = Expense
    template_name = "expense_tracker/list.html"
    context_object_name = "expenses"
    ordering = ["-created_at"]

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.GET.get("date")
        category = self.request.GET.get("category")
        search = self.request.GET.get("search")

        if date:
            queryset = queryset.filter(created_at__date=date)
        if category:
            queryset = queryset.filter(category=category)
        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        total = self.get_queryset().aggregate(
            total_sum=Sum(F("amount") * F("quantity"))
        )
        data["total"] = total["total_sum"] or 0

        data["category"] = Expense.my_dict

        category_totals = (
            self.get_queryset()
            .values("category")
            .annotate(total=Sum(F("amount") * F("quantity")))
            .order_by("-total")
        )
        data["category_totals"] = list(category_totals)

        return data


class ExpenseCreateView(CreateView):
    model = Expense
    template_name = "expense_tracker/create.html"
    fields = "__all__"
    success_url = reverse_lazy("expense-list")


class BudgetListView(ListView):
    model = Budget
    template_name = "expense_tracker/budget_list.html"
    context_object_name = "budgets"
    ordering = ["-start_date"]
    
    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
        budgets=self.get_queryset()
        
        for i in budgets:
            tmp= Expense.objects.filter(
                category=i.category).aggregate(
                total_sum=Sum(F("amount") * F("quantity")))["total_sum"]
            i.spends=tmp
        data['budgets']=budgets
        return data
    
            
        
    