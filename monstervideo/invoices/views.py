from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

def index(request):
    customer_list = Customer.objects.order_by('name')
    context = { 'customer_list': customer_list }
    return render(request, 'invoices/index.html', context)