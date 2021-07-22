from django.db import models


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    market_price = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'products'


class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer = models.CharField(max_length=50)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=25)
    shipping_name = models.CharField(max_length=50, null=True)
    shipping_address = models.TextField(null=True)
    contact = models.CharField(max_length=10, null=True)
    products = models.ManyToManyField(Products)

    def __str__(self):
        return self.customer

    class Meta:
        db_table = 'orders'
        unique_together = (('customer', 'order_date', 'status'),)


class OrderStatus(models.Model):
    order_id = models.IntegerField()
    chgdate = models.DateTimeField()
    status = models.CharField(max_length=25)

    def __str__(self):
        return self.status

    class Meta:
        managed = False
        db_table = 'order_status'

