from django.urls import include, path
from . import views

app_name = "orders"

urlpatterns = [
    path('orders/', views.ListOrders, name='order_list'),
    path('orders/<int:order_id>/', views.OrderDetails, name='order_details'),
    path('orders/filterstatus', views.filterstatus, name='filterstatus'),
]
