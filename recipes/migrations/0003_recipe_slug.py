# Generated by Django 4.1.4 on 2023-01-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_alter_recipe_author_alter_recipeingredient_unit"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="slug",
            field=models.SlugField(null=True, unique=True),
        ),
    ]
