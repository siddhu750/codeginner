# Generated by Django 2.2 on 2022-10-01 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeginnerApp', '0007_auto_20221001_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentregister',
            name='slug',
        ),
    ]
