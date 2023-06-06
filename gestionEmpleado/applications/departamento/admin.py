
from django.contrib import admin
from .models import ApartModel

# Register your models here.



@admin.register(ApartModel)
class ApartAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = (
        'id',
        'name',)
