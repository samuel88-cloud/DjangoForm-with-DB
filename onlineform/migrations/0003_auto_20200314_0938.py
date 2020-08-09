# Generated by Django 2.2.6 on 2020-03-14 04:08

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineform', '0002_auto_20200313_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetails',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
