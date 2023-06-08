from django.db import models

# Create your models here.

class ApartModel(models.Model):
    """Model definition for EmployeeModel."""

    # TODO: Define fields here

    name = models.CharField(
        'Name', 
        max_length=50,
    )
    short_name = models.CharField(
        'Abbreviation', 
        max_length=50,
    )

    
    class Meta:
        """Meta definition for ApartModel."""

        verbose_name = 'Apartmen'
        verbose_name_plural = 'Apartmens'
        ordering = ['id']
        unique_together = ['name','short_name']

    def __str__(self):
        """Unicode representation of Apartmen."""
        
        return self.name
    
