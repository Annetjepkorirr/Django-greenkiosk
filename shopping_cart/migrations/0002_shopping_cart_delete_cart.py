# Generated by Django 4.2.3 on 2023-08-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_vendor'),
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=30)),
                ('quantity', models.PositiveIntegerField()),
                ('products', models.ManyToManyField(to='inventory.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
