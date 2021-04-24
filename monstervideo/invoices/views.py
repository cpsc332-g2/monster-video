from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer, Appraisal, Proposal, Warranty, Installation, Employee, Speakers, AVComponents, Electronics, Item

def index(request):
    customer_list = Customer.objects.order_by('name')
    context = { 'customer_list': customer_list }
    return render(request, 'invoices/index.html', context)

def details(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    context = { 
        'customer': customer,
    }
    appraisal_list = Appraisal.objects.all()
    if(appraisal_list):
        for appraisal in appraisal_list:
            if appraisal.customer_id == customer_id:
                context['appraisal'] = appraisal

    return render(request, 'invoices/customer.html', context)

def add_customer(request):
    if request.method=="POST":
        customer = Customer()
        customer.name = request.POST.get('name')
        customer.street = request.POST.get('street')
        customer.city = request.POST.get('city')
        customer.state = request.POST.get('state')
        customer.zipCode = request.POST.get('zipCode')
        customer.number = request.POST.get('number')
        customer.save()
        return redirect('/invoices')
    else:
        return redirect('/invoices')

def add_appraisal(request, customer_id):
    if request.method=="POST":
        customer = get_object_or_404(Customer, pk=customer_id)
        appraisal = Appraisal()
        appraisal.customer = customer
        appraisal.location = request.POST.get('location')
        appraisal.cableRun = request.POST.get('cableRun')
        appraisal.comments = request.POST.get('comments')
        appraisal.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")