from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import EmployeeModel


class PersonListView(ListView):
    model = EmployeeModel
    template_name = "staff/list_peopels.html"
    paginate_by = 10
    context_object_name = 'peoples'
    
