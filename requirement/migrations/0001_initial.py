# Generated by Django 3.0.5 on 2020-05-07 15:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applicants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(default='', max_length=42)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(default='', max_length=20)),
                ('area', models.CharField(default='', max_length=150)),
                ('marital_status', models.CharField(default='Unmarried', max_length=20)),
                ('qualification', models.CharField(default='', max_length=200)),
                ('experience', models.CharField(default='', max_length=100)),
                ('present_company', models.CharField(default='', max_length=150)),
                ('current_salary', models.CharField(default='', max_length=20)),
                ('expected_salary', models.CharField(default='', max_length=20)),
                ('job_location', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'applicants',
            },
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(default='', max_length=42)),
                ('address', models.CharField(max_length=500)),
                ('company_name', models.CharField(default='', max_length=150)),
                ('phone', models.CharField(max_length=20)),
                ('company_phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('status', models.CharField(default='Inactive', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('company_name', models.CharField(default='', max_length=400)),
                ('job_tittle', models.CharField(default='', max_length=400)),
                ('location', models.CharField(max_length=500)),
                ('experience', models.CharField(max_length=500)),
                ('salary', models.CharField(max_length=500)),
                ('requirement', models.CharField(max_length=500)),
                ('applicants', models.PositiveSmallIntegerField(default=0)),
                ('list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=10)),
            ],
            options={
                'db_table': 'job',
            },
        ),
    ]