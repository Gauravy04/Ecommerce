# Generated by Django 5.1.7 on 2025-03-19 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
    ]
