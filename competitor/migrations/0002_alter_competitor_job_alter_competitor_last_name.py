# Generated by Django 4.2.7 on 2023-11-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='job',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]