# Generated by Django 5.0.3 on 2024-03-20 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcollage', '0003_alter_user_employee_create_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='employee',
            new_name='is_employee',
        ),
        migrations.DeleteModel(
            name='Create_Employee',
        ),
    ]
