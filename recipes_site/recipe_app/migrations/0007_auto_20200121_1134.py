# Generated by Django 3.0.2 on 2020-01-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0006_auto_20200121_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='direction',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient',
            field=models.TextField(),
        ),
    ]
