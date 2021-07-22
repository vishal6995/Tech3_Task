# Generated by Django 3.2.5 on 2021-07-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_orders_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='shipping_address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='shipping_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]