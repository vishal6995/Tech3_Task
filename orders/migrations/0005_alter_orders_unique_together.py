# Generated by Django 3.2.5 on 2021-07-21 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orders_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orders',
            unique_together={('customer', 'order_date', 'status')},
        ),
    ]