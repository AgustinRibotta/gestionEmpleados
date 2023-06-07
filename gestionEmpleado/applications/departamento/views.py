from django.shortcuts import render
from django.views.generic import ListView

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
