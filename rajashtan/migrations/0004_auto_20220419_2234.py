# Generated by Django 3.0.5 on 2022-04-19 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rajashtan', '0003_auto_20220415_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rajashtan',
            name='cafes',
            field=models.CharField(max_length=1020),
        ),
        migrations.AlterField(
            model_name='rajashtan',
            name='hotels',
            field=models.CharField(max_length=1020),
        ),
    ]
