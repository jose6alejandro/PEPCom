# Generated by Django 3.2.5 on 2021-09-03 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crud_problems_app', '0005_remove_user_create_problem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_create_problem',
            name='user',
            field=models.ForeignKey(default=27, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
