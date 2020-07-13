from django.shortcuts import render , get_object_or_404
from django.shortcuts import HttpResponse
from .models import Order
from django.core.paginator import Paginator

def show_orders(requests):
    if(requests.method == 'GET'):
        search = requests.GET.get('search')
        date_from = requests.GET.get('from')
        to =  requests.GET.get('to')
        if(search != None):
            orders = Order.objects.all().filter(order_name__contains=search)
            if(date_from != None and to != None and date_from != '' and to != ''):
                orders = orders.filter(created_at__range=[date_from, to])
        else:
            orders = Order.objects.all()
            if(date_from != None and to != None and date_from != '' and to != ''):
                orders = orders.filter(created_at__range=[date_from, to])
        
    else:
        orders = Order.objects.all()

    paginator = Paginator(orders , 5)
    page = requests.GET.get('page')
    orders = paginator.get_page(page)

    return render(requests , "orders/orders.html" , {"orders": orders})
