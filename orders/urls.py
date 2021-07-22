from django.urls import include, path
from rest_framework import routers
from . import views

app_name = "orders"
router = routers.DefaultRouter()
router.register(r'api-orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/', views.ListOrders, name='order_list'),
    path('orders/<int:order_id>/', views.OrderDetails, name='order_details'),
    path('orders/filterstatus', views.filterstatus, name='filterstatus'),
]
