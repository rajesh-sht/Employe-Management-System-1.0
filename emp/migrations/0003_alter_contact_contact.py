# Generated by Django 4.2.4 on 2023-08-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_contact_alter_employee_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.CharField(max_length=20),
        ),
    ]
