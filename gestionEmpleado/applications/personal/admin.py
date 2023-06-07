from django.contrib import admin
from .models import EmployeeModel, SkillsModels

# Register your models here.

@admin.register(SkillsModels)
class SkillAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = (
        'id',
        'skill',
    )

@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    '''Admin View for EmployeeModel'''

    list_display = (
        'id',
        'first_name',
        'last_name',
        'apart',
        'full_name',
        )
    list_filter = ('apart',)

    def full_name(self,obj):
        return obj.first_name  + ' ' + obj.last_name
    
    search_fields = (
        'first_name',
        'last_name',
    )
    filter_horizontal = ('skill',)