from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OrdersSerializer
from .models import Orders, OrderStatus, Products
# from drf_multiple_model.views import ObjectMultipleModelAPIView


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('customer')
    serializer_class = OrdersSerializer

# class OrderDetailsViewSet(viewsets.ModelViewSet):
#     queryset = Orders.objects.get()
#     serializer_class = OrdersSerializer


def ListOrders(request):
    orders = Orders.objects.all()

    args = {
        'orders': orders
    }

    return render(request, "Orders/orders_list.html", args)

def OrderDetails(request,order_id):
    order_details = Orders.objects.get(order_id=order_id)
    status_history = OrderStatus.objects.filter(order_id=order_id).order_by('chgdate')
    product_list = Products.objects.filter(orders=order_id)

    args = {
        'order_details':order_details,
        'status_history':status_history,
        'product_list':product_list,
    }

    return render(request, "Orders/order_details.html", args)
