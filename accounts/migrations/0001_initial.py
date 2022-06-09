# Generated by Django 4.0.5 on 2022-06-09 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symboling', models.IntegerField(blank=True, max_length=4, null=True, unique=True)),
                ('make', models.CharField(blank=True, max_length=100, null=True)),
                ('fueltype', models.CharField(blank=True, max_length=10, null=True)),
                ('numofdoors', models.CharField(blank=True, max_length=10, null=True)),
                ('bodystyle', models.CharField(blank=True, max_length=10, null=True)),
                ('drivewheels', models.CharField(blank=True, max_length=10, null=True)),
                ('enginelocation', models.CharField(blank=True, max_length=10, null=True)),
                ('wheelbase', models.FloatField(default=False)),
                ('price', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
