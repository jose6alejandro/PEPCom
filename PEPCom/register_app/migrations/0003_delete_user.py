# Generated by Django 3.2.5 on 2021-08-16 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
