# Generated by Django 2.0.6 on 2018-06-28 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0015_auto_20180627_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='password',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='username',
        ),
    ]
