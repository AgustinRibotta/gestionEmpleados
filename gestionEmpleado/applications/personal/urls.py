from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    path(
        'upgrade-people/<pk>',
        PeopleUpdateView.as_view(),
        name='People-upgrade'
    ),
    path(
        'delete-people/<pk>',
        PeopleDeleteView.as_view(),
        name='People-delete'
    ),
    path(
        'create-people/',
        PeopleCreateView.as_view(),
        name='People-create'
    ),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
