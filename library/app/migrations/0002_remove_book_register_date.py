# Generated by Django 5.1.6 on 2025-02-18 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='register_date',
        ),
    ]
