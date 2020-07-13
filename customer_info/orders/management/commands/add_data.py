from orders.models import Order , Customer , Company
from django.core.management.base import BaseCommand
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print(BASE_DIR)
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path (or a Python file object)
        insert_count1 = Company.objects.from_csv( BASE_DIR+'\data\Test task - Mongo - customer_companies.csv')
        insert_count2 = Customer.objects.from_csv(BASE_DIR+'\data\Test task - Mongo - customers.csv')
        insert_count3 = Order.objects.from_csv(BASE_DIR+'\data\Test task - Orders.csv')
        print( "{} records inserted".format(insert_count1+insert_count2+insert_count3))
