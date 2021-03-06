# Generated by Django 3.2.5 on 2021-09-09 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('statistics_app', '0004_my_skills_correct_answers'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('january', models.IntegerField(blank=True, default=0)),
                ('february', models.IntegerField(blank=True, default=0)),
                ('march', models.IntegerField(blank=True, default=0)),
                ('april', models.IntegerField(blank=True, default=0)),
                ('may', models.IntegerField(blank=True, default=0)),
                ('june', models.IntegerField(blank=True, default=0)),
                ('july', models.IntegerField(blank=True, default=0)),
                ('august', models.IntegerField(blank=True, default=0)),
                ('september', models.IntegerField(blank=True, default=0)),
                ('october', models.IntegerField(blank=True, default=0)),
                ('november', models.IntegerField(blank=True, default=0)),
                ('december', models.IntegerField(blank=True, default=0)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
