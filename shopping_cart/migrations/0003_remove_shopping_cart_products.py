# Generated by Django 4.2.3 on 2023-09-11 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shopping_cart", "0002_shopping_cart_delete_cart"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shopping_cart",
            name="products",
        ),
    ]
