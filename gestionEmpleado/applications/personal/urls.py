from django.urls import path

from .views import *

app_name = 'persona_app'

urlpatterns = [
    path(
        'list-peoples/', 
        PersonListView.as_view(), 
        name='Peoples',
    ),
    path(
        'detail-people/<pk>/',
        PersonDetailView.as_view(),
        name='People-detail'
    ),
    path(
        'apart-people/<short_name>',
        PersonByKwordListView.as_view(),
        name='Apart-people'
    ),
]
