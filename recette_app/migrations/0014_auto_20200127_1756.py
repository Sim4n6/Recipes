# Generated by Django 3.0.2 on 2020-01-27 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recette_app', '0013_auto_20200127_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activite',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='Photos'),
        ),
    ]
