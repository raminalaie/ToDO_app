# Generated by Django 4.0.2 on 2023-03-12 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_id_number_customuser_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='number',
        ),
    ]