# Generated by Django 4.2.2 on 2023-06-05 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Apartmen',
                'verbose_name_plural': 'Apartmens',
                'ordering': ['id'],
            },
        ),
    ]
