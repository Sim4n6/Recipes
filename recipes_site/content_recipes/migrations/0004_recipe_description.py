# Generated by Django 3.0.2 on 2020-01-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_recipes', '0003_auto_20200113_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='Description'),
            preserve_default=False,
        ),
    ]
