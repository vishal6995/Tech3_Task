# Generated by Django 3.2.5 on 2021-07-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer', models.CharField(max_length=50)),
                ('order_date', models.DateTimeField()),
                ('status', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
    ]
