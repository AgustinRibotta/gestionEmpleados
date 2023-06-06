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
        'name',
        'first_name',
        'apart',
        'full_name',
        )
    list_filter = ('apart',)

    def full_name(self,obj):
        return obj.name  + ' ' + obj.first_name
    
    search_fields = (
        'name',
        'first_name',
    )
    filter_horizontal = ('skill',)