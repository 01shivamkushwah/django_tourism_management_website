# Generated by Django 3.0.5 on 2022-04-19 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('famousplace', '0002_auto_20220419_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famousplace',
            name='hotels',
            field=models.CharField(max_length=11200),
        ),
    ]
