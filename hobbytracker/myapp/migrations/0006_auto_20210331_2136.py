# Generated by Django 3.1.7 on 2021-03-31 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210331_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbytime',
            name='endTime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hobbytime',
            name='startTime',
            field=models.IntegerField(),
        ),
    ]
