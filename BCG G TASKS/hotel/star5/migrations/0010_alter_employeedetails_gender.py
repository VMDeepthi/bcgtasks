# Generated by Django 4.1.7 on 2023-03-01 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star5', '0009_alter_employeedetails_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='GENDER',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True),
        ),
    ]
