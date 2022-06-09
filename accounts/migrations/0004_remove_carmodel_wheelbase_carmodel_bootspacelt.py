# Generated by Django 4.0.5 on 2022-06-09 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_carmodel_wheelbase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='wheelbase',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='bootspacelt',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
    ]
