# Generated by Django 3.2.5 on 2021-07-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20210721_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chgdate', models.DateTimeField()),
                ('status', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'order_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('market_price', models.IntegerField()),
            ],
            options={
                'db_table': 'produts',
                'managed': False,
            },
        ),
    ]
