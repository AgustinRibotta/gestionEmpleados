# Generated by Django 4.2.2 on 2023-06-05 20:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_remove_employeemodel_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='cv',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
