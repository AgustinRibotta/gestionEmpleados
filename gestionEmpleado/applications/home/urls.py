
from django.urls import path

from applications.home.views import HomeView

app_name = 'home_app'


urlpatterns = [
    path(
        '',
        HomeView.as_view(), 
        name='Start'
    ),

]
