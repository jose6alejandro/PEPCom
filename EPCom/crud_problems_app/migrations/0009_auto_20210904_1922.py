# Generated by Django 3.2.5 on 2021-09-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_problems_app', '0008_alter_user_create_problem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_create_problem',
            name='correct_option',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='user_create_problem',
            name='distractor1',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='user_create_problem',
            name='distractor2',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='user_create_problem',
            name='distractor3',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='user_create_problem',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='user_create_problem',
            name='question',
            field=models.CharField(max_length=100),
        ),
    ]
