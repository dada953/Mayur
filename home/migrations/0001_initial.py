# Generated by Django 5.1 on 2024-09-04 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=14)),
                ('lastName', models.CharField(max_length=10)),
                ('mobileno', models.IntegerField(max_length=10)),
            ],
        ),
    ]
