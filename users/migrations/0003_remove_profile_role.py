# Generated by Django 4.2.11 on 2024-05-12 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_address_profile_role_manager_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
    ]
