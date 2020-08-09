# Generated by Django 2.2.6 on 2020-03-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=12)),
                ('client_value', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=50)),
            ],
        ),
    ]