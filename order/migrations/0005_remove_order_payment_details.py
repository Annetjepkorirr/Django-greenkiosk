# Generated by Django 4.2.3 on 2023-08-04 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_remove_order_delivery_order_delivery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_details',
        ),
    ]
