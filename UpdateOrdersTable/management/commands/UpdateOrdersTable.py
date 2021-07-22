from django.core.management.base import BaseCommand
import requests
import json
from orders.models import Orders, Products, OrderStatus
from django.db.models import Q


class Command(BaseCommand):
    help = 'Update Orders Table from API'

    api_url = "http://ec2-18-217-116-137.us-east-2.compute.amazonaws.com/rest/default/V1/orders?searchCriteria%5BcurrentPage%5D=1&searchCriteria%5BpageSize%5D=25"

    headers = {
        'authorization': 'Bearer 6hby2nljxjoc6xe5a03240kkih2g9inv',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'postman-token': '496aabd6-f70e-3bc7-14f3-4356773c875b',
        'Cookie': 'PHPSESSID=gvbkfuqsu5hs3aig8l9i34r56m'
    }

    print("Accessing API..")
    response = requests.get(api_url, headers=headers)
    print(response)
    order_details = json.loads(response.text)

    def add_product(self):

        for order in self.order_details['items']:
            for product in order['items']:
                product_id = product['product_id']
                product_name = product['name']
                market_price = product['price']

                # print(product_id, "|", product_name, "|", market_price, "|")

                (updateProductValues, created) = Products.objects.get_or_create(id=product_id,
                                                                                    name=product_name,
                                                                                    market_price=market_price)

                if created:
                    updateProductValues.save()
                    print(updateProductValues, "|", 'Added to DB')

    def update_status_history(self):

        for order in self.order_details['items']:
            for history in order['status_histories']:
                order_id = history['parent_id']
                chgdate = history['created_at']
                order_status = history['status']

                # print(order_id, "|", chgdate, "|", order_status, "|")

                (updateOrderValues, created) = OrderStatus.objects.get_or_create(order_id=order_id, chgdate=chgdate, status=order_status)

                if created:
                    updateOrderValues.save()
                    print(updateOrderValues, "|", 'Added to DB')

    def update_order(self):

        for order in self.order_details['items']:
            order_id = order['entity_id']
            name = order['customer_firstname']+" "+order['customer_lastname']
            order_created = order['created_at']
            status = order['status']
            shipping_address_obj = order['extension_attributes']['shipping_assignments'][0]['shipping']['address']
            shipping_name = shipping_address_obj['firstname']+" "+shipping_address_obj['lastname']
            shipping_address = shipping_address_obj['street'][0]+","+shipping_address_obj['city']+","+shipping_address_obj['region']
            contact = shipping_address_obj['telephone']

            product_items_obj = order['items']
            product_ids = []
            for product in product_items_obj:
                product_ids.append(product['product_id'])


            # print(order_id, "|", name, "|", order_created, "|", status, "|", shipping_name, "|", shipping_address, "|", contact, "|", product_ids)

            (updateValues, created) = Orders.objects.get_or_create(order_id=order_id, customer=name, order_date=order_created, status=status, shipping_name=shipping_name, shipping_address=shipping_address, contact=contact)
            updateValues.products.add(Products.objects.get(id__in=product_ids))
            if created:
                updateValues.save()
                print(updateValues, "|", 'Added to DB')
            else:
                print('Already exits')
            # try:
            #     updateValue = Orders.objects.get(customer=name, order_date=order_created)
            # except Orders.DoesNotExist:
            #     obj = Orders(customer=name, order_date=order_created, status=status)
            #     obj.save()

    def handle(self, *args, **kwargs):
        self.add_product()
        self.update_status_history()
        self.update_order()
