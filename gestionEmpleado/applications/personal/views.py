from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)
from django.urls import reverse_lazy
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
    

class PeopleUpdateView(UpdateView):
    model = EmployeeModel
    template_name = "staff/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'apart',
        'cv',
        'skill',
    ]
    success_url = reverse_lazy ('persona_app:Peoples')
    context_object_name = 'upgrade'
    
    



class PeopleDeleteView(DeleteView):
    model = EmployeeModel
    template_name = "staff/delete.html"
    success_url = reverse_lazy ('persona_app:Peoples')



class PeopleCreateView(CreateView):
    model = EmployeeModel
    template_name = "staff/create.html"
    fields =[
        'first_name',
        'last_name',
        'job',
        'apart',
        'skill',
        'cv',
    ]
    success_url = reverse_lazy ('persona_app:Peoples')


