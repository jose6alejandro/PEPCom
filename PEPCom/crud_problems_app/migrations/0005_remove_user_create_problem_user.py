# Generated by Django 3.2.5 on 2021-09-03 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_problems_app', '0004_alter_user_create_problem_explanation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_create_problem',
            name='user',
        ),
    ]
