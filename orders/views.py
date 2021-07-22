from django.shortcuts import render
from .models import Orders, OrderStatus, Products


def ListOrders(request):
    orders = Orders.objects.all()

    status_list = OrderStatus.objects.values('status').distinct()

    args = {
        'orders': orders,
        'status_list': status_list,
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

def filterstatus(request):
    status_val = request.GET.get('status')
    if status_val != 'All':
        orders = Orders.objects.all().filter(status=status_val)
    else:
        orders = Orders.objects.all()
    print("[ORDERS:]",orders)
    args={
        'orders': orders,
    }
    return render(request, "orders/filterstatus.html", args)
