from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView,
    DetailView,
)

from .models import EmployeeModel


class PersonListView(ListView):
    template_name = "staff/list_peopels.html"
    paginate_by = 10
    context_object_name = 'peoples'
    
    def get_queryset(self):
        kword = self.request.GET.get('kword','')
        planta = EmployeeModel.objects.filter(
        last_name__icontains= kword.capitalize(),
        )
            
        return planta


class PersonDetailView(DetailView):
    model = EmployeeModel
    template_name = "staff/detail.html"
    context_object_name = 'detail'
    


class PersonByKwordListView(ListView):
    model = EmployeeModel
    template_name = "staff/list_bykword.html"
    context_object_name = 'bykword'
    
    def get_queryset(self):
        apart = self.kwargs['short_name']
        people_apart = EmployeeModel.objects.filter(
            apart__short_name = apart
        )
        
        return people_apart


