# Generated by Django 2.0.6 on 2018-06-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinet',
            name='estimated_age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='clinet',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
    ]