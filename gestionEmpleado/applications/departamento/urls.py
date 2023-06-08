from django.urls import path

from applications.departamento.views import *

app_name = 'departamento_app'

urlpatterns = [
    path(
        'list-apart/',
        ApartListView.as_view(),
        name='Apartmens'
    ),
    path(
        'update-apart/<pk>/',
        ApartUpdateView.as_view(),
        name='Update-apart'
    ),
    path(
        'delete-apart/<pk>/',
        ApartDeleteView.as_view(),
        name='Delete-apart'
    ),
    path(
        'create-apart/',
        ApartCreateView.as_view(),
        name='Create-apart'
    ),

]
