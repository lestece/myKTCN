# Generated by Django 3.2.18 on 2023-03-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.IntegerField(choices=[(0, 'Easy'), (1, 'Moderate'), (2, 'Expert')], default=0),
        ),
    ]
