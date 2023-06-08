from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DeleteView, 
    DetailView,
    UpdateView,
    CreateView,
)

from applications.departamento.models import ApartModel
# Create your views here.


class ApartListView(ListView):
    template_name = "departamento/list_apart.html"
    paginate_by = 10
    context_object_name = 'apart'
    
    def get_queryset(self):
        kword = self.request.GET.get('kword','')
        planta = ApartModel.objects.filter(
        name__icontains= kword.capitalize(),
        )
            
        return planta


class ApartUpdateView(UpdateView):
    model = ApartModel
    template_name = "departamento/update.html"
    fields = [
        'name',
        'short_name',
    ]
    success_url = reverse_lazy ('departamento_app:Apartmens')
    context_object_name = 'upgrade'


class ApartDeleteView(DeleteView):
    model = ApartModel
    template_name = "departamento/delete.html"
    success_url = reverse_lazy ('departamento_app:Apartmens')


class ApartCreateView(CreateView):
    model = ApartModel
    template_name = "departamento/create.html"
    fields =[
        'name',
        'short_name',
    ]
    success_url = reverse_lazy ('departamento_app:Apartmens')


