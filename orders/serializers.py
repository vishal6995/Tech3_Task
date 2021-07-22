from rest_framework import serializers
from .models import Orders, OrderStatus, Products


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = ('order_id', 'customer', 'order_date', 'shipping_name', 'shipping_address', 'contact')


class OrderStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ('chgdate', 'status')


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'market_price')
