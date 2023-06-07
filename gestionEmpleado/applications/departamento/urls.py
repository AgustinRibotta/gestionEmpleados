from django.urls import path

from applications.departamento.views import ApartListView

app_name = 'departamento_app'

urlpatterns = [
    path(
        'list-apart/',
        ApartListView.as_view(),
        name='Apartmens'
    ),

]
