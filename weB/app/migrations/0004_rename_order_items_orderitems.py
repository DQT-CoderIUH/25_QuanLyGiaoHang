# Generated by Django 4.1.3 on 2023-05-06 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_address_nh'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order_items',
            new_name='Orderitems',
        ),
    ]
