# Generated by Django 5.1.2 on 2024-10-28 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bankloan',
            fields=[
                ('Name', models.CharField(max_length=10)),
                ('Accountno', models.IntegerField(primary_key='Accountno', serialize=False)),
                ('Interest', models.FloatField()),
                ('Startdate', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('Mobilenumber', models.IntegerField()),
                ('Amount', models.IntegerField()),
                ('Enddate', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
