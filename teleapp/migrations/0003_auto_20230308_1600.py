# Generated by Django 3.1 on 2023-03-08 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teleapp', '0002_auto_20230306_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='members',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teleapp.team'),
        ),
    ]
