# Generated by Django 4.1.4 on 2023-01-06 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0004_alter_recipe_author_alter_recipeingredient_recipe"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipeingredient",
            name="unit",
            field=models.IntegerField(
                choices=[(0, "GRAM"), (1, "MILLILITR"), (2, "DONA")]
            ),
        ),
    ]