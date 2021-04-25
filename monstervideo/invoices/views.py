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

#Note: The redirect stays the same for each entity
# customer_id has to be passed to each function below

#May need to edit the parameters and code for each defined functions below
#appraisal is FK of Proposal
def add_proposal(request, customer_id):
    if request.method=="POST":
        appraisal = get_object_or_404(Customer, pk=customer_id)     #Unsure
        proposal = Proposal()
        proposal.appraisal = appraisal
        proposal.date = request.POST.get('date')
        proposal.description = request.POST.get('description')
        proposal.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

#proposal and customer are FK of installation 
def add_installation(request, customer_id):
    if request.method=="POST":
        proposal = get_object_or_404(Customer, pk=customer_id) #unsure
        customer = get_object_or_404(Customer, pk=customer_id)  #unsure
        installation = Installation()
        installation.proposal = proposal
        installation.customer = customer
        installation.date_start = request.POST.get('date_start')
        installation.date_finish = request.POST.get('date_finish')
        installation.cleanup = request.POST.get('cleanup')
        installation.total_material = request.POST.get('total_material')
        installation.total_labor = request.POST.get('total_labor')
        installation.total_cost = request.POST.get('total_cost')
        installation.cables_cost = request.POST.get('cables_cost')
        installation.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")
 
#installation is FK of Employee 
def add_employee(request, customer_id):
    if request.method=="POST":
        installation = get_object_or_404(Customer, pk=customer_id)  #unsure
        employee = Employee()
        employee.installation = installation
        employee.name = request.POST.get('name')
        employee.department = request.POST.get('department')
        employee.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

#installation is the FK for Item 
def add_item(request, customer_id):
    if request.method=="POST":
        installation = get_object_or_404(Customer, pk=customer_id)  #unsure
        item = Item()
        item.installation = installation
        item.item_description = request.POST.get('item_description')
        item.item_location = request.POST.get('item_location')
        item.item_name = request.POST.get('item_name')
        item.item_quanity = request.POST.get('item_quanity')
        item.item_labor_cost = request.POST.get('item_labor_cost')
        item.item_cost = request.POST.get('item_cost')
        item.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")
 
#Speaker, AVComponents, and elctronics inherit attributes from class item (Polymorphism/Inheritance)
#How to implement?

def add_speakers(request, customer_id):
    if request.method=="POST":
        installation = get_object_or_404(Customer, pk=customer_id)  #unsure
        speakers = Speakers()
        speaker.installation = installation
        speakers.total = request.POST.get('total')
        speakers.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")
 
def add_avcomponents(request, customer_id):
    if request.method=="POST":
        installation = get_object_or_404(Customer, pk=customer_id)  #unsure
        avcomponents = AVComponents()
        avcomponents.installation = installation
        avcomponents.total = request.POST.get('total')
        avcomponents.save()
        return redirect(f"/invoices/{customer_id}")
    else:
       return redirect(f"/invoices/{customer_id}")
 
def add_electronics(request, customer_id):
    if request.method=="POST":
        installation = get_object_or_404(Customer, pk=customer_id)  #unsure
        electronics = Electronics()
        electronics.installation = installation
        electronics.total = request.POST.get('total')
        electronics.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

#item is FK of Warranty 
def add_warranty(request, customer_id):
    if request.method=="POST":
        item = get_object_or_404(Customer, pk=customer_id)  #unsure
        warranty = Warranty()
        warranty.item = item
        warranty.start_date = request.POST.get('start_date')
        warranty.title = request.POST.get('title')
        warranty.mfg_warranty = request.POST.get('mfg_warranty')
        warranty.add_warranty = request.POST.get('add_warranty')
        warranty.cost = request.POST.get('cost')
        warranty.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")
