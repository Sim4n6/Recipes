# Generated by Django 3.0.2 on 2020-01-13 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recette_app', '0002_auto_20200113_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='directions',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=200)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recette_app.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(max_length=200)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recette_app.Recipe')),
            ],
        ),
    ]
