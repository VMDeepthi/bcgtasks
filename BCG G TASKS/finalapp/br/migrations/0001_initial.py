# Generated by Django 4.1.3 on 2023-02-11 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empdata',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=30)),
                ('doj', models.CharField(max_length=20)),
                ('expsalary', models.IntegerField()),
                ('prevexp', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
            ],
        ),
    ]
