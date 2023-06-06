from django.db import models

from applications.departamento.models import ApartModel
from ckeditor.fields import RichTextField

# Create your models here.


class SkillsModels(models.Model):
    """Model definition for SkillsModels."""

    # TODO: Define fields here
    
    skill = models.CharField(
        'Skill', 
        max_length=50
    )

    class Meta:
        """Meta definition for SkillsModels."""

        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['id']
        unique_together = ['skill']

    def __str__(self):
        """Unicode representation of SkillsModels."""
        return str(self.id) + ' '  + self.skill


class EmployeeModel(models.Model):
    """Model definition for EmployeeModel."""

    # TODO: Define fields here

    name = models.CharField(
        'Name', 
        max_length=50,
    )
    first_name = models.CharField(
        'First Name', 
        max_length=50,
    )
    job = models.CharField(
        'Position', 
        max_length=50
    )
    apart = models.ForeignKey(
        ApartModel, 
        on_delete=models.CASCADE,
    )
    skill = models.ManyToManyField(
        SkillsModels
    )
    cv = RichTextField(
        blank= True,
    )
    
    class Meta:
        """Meta definition for EmployeeModel."""

        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        """Unicode representation of EmployeeModel."""
        return str(self.id) + ' ' + self.name + ' ' + self.first_name