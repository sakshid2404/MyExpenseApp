from django.urls import path
from .views import (
    ExpenseListView, ExpenseCreateView
)

urlpatterns = [
    path("", ExpenseListView.as_view(), name="expense-list"),
    path("add/", ExpenseCreateView.as_view(), name="expense-add"),
]
