# Generated by Django 3.0.2 on 2020-01-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recette_app', '0005_recipe_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
