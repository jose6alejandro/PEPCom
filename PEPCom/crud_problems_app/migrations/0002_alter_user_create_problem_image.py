# Generated by Django 3.2.5 on 2021-09-03 04:17

import crud_problems_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_problems_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_create_problem',
            name='image',
            field=models.ImageField(null=True, upload_to=crud_problems_app.models.user_directory_path),
        ),
    ]