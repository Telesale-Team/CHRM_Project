# Generated by Django 3.1 on 2023-03-10 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teleapp', '0008_alter_team_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='expenses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='income',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='room_fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
