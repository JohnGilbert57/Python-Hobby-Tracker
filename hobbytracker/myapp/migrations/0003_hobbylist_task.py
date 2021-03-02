# Generated by Django 3.1.6 on 2021-03-01 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_delete_userhobby'),
    ]

    operations = [
        migrations.CreateModel(
            name='HobbyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(max_length=200)),
                ('goal', models.FloatField()),
                ('hobbylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.hobbylist')),
            ],
        ),
    ]
