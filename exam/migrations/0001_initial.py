# Generated by Django 5.1.4 on 2025-03-20 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(choices=[('Week Test', 'Week Test'), ('Monthly Test', 'Monthly Test'), ('Unit Test', 'Unit Test'), ('Progress Test ', 'Progress Test'), ('Oral Test', 'Oral Test'), ('Quaterly Exam', 'Quaterly Exam'), ('Half-Yearly Exam', 'Half-Yearly Exam'), ('Annual Exam', 'Annual Exam')], max_length=50)),
                ('exam_date', models.DateField()),
                ('start_time', models.CharField(choices=[('08:00 AM', '08:00 AM'), ('10:00 AM', '10:00 AM'), ('12:00 PM', '12:00 PM'), ('02:00 PM', '02:00 PM'), ('04:00 PM', '04:00 PM')], max_length=10)),
                ('end_time', models.CharField(choices=[('08:00 AM', '08:00 AM'), ('10:00 AM', '10:00 AM'), ('12:00 PM', '12:00 PM'), ('02:00 PM', '02:00 PM'), ('04:00 PM', '04:00 PM')], max_length=10)),
            ],
        ),
    ]
