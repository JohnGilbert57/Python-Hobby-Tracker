# Generated by Django 3.1.7 on 2021-03-31 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210305_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='hobbyUser',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='spriteId',
            field=models.CharField(max_length=300),
        ),
    ]
