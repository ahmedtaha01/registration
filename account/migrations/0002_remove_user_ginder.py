# Generated by Django 4.1.1 on 2022-09-17 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ginder',
        ),
    ]
