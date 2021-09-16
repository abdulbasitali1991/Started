# Generated by Django 3.2.7 on 2021-09-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=221)),
                ('Last_Name', models.CharField(max_length=224)),
                ('Department', models.CharField(max_length=225)),
                ('Experience', models.IntegerField()),
                ('Salary', models.BigIntegerField()),
                ('Date_OF_Joinig', models.DateField()),
            ],
        ),
    ]
