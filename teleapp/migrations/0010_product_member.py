# Generated by Django 3.1 on 2023-03-10 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teleapp', '0009_auto_20230310_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='member',
            field=models.IntegerField(default=0),
        ),
    ]