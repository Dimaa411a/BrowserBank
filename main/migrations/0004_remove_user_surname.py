# Generated by Django 5.1.6 on 2025-03-06 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_user_email_alter_user_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='surname',
        ),
    ]
