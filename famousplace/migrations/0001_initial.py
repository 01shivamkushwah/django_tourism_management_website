# Generated by Django 3.0.5 on 2022-04-18 11:18

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='famousplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', tinymce.models.HTMLField()),
                ('hotels', models.CharField(max_length=100)),
                ('cafes', models.CharField(max_length=100)),
                ('image', models.ImageField(default=None, max_length=250, null=True, upload_to='famousplace/')),
            ],
        ),
    ]
