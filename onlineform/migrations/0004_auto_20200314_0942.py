# Generated by Django 2.2.6 on 2020-03-14 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineform', '0003_auto_20200314_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetails',
            name='website',
            field=models.URLField(),
        ),
    ]
