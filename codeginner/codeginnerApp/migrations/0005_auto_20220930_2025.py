# Generated by Django 2.2 on 2022-09-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeginnerApp', '0004_auto_20220930_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentregister',
            name='chExample',
            field=models.URLField(),
        ),
    ]
