from django.urls import path

from .views import PersonListView

app_name = 'persona_app'

urlpatterns = [
    path(
        'list-peoples/', 
        PersonListView.as_view(), 
        name='Peoples',
    ),
]
