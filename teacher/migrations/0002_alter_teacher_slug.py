# Generated by Django 4.2.7 on 2023-11-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
