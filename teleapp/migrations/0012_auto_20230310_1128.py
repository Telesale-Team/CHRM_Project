# Generated by Django 3.2.4 on 2023-03-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teleapp', '0011_auto_20230310_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='Bank_Code',
        ),
        migrations.AddField(
            model_name='expenses',
            name='account_bank',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
