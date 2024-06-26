# Generated by Django 5.0.3 on 2024-03-07 05:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_management', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_role', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='email address')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('is_staff', models.BooleanField(blank=True, default=False, null=True)),
                ('is_admin', models.BooleanField(blank=True, default=False, null=True)),
                ('is_superuser', models.BooleanField(blank=True, default=False, null=True)),
                ('employee', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('target_per_month', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appcollage.branch_management')),
                ('employee_role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appcollage.employee_role')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
