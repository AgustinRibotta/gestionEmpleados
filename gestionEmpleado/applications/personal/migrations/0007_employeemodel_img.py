# Generated by Django 4.2.2 on 2023-06-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_alter_employeemodel_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='people', verbose_name='Avatar'),
        ),
    ]