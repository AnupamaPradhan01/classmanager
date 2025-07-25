# Generated by Django 5.1.4 on 2025-03-20 12:33

import django.core.validators
import timetable.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_no', models.CharField(choices=[('Nursery', 'Nursery'), ('KG', 'KG'), ('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th'), ('11th', '11th'), ('12th', '12th')], max_length=100)),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=50)),
                ('timetable_file', models.FileField(upload_to=timetable.models.timetable_upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xls', 'xlsx'])])),
            ],
        ),
    ]
