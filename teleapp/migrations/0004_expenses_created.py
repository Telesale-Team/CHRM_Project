# Generated by Django 3.1 on 2023-03-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teleapp', '0003_auto_20230308_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
