# Generated by Django 3.1.7 on 2021-03-31 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210331_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='spriteId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.sprite'),
        ),
    ]
