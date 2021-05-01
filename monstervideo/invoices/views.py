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
                proposal_list = Proposal.objects.all()
                if(proposal_list):
                    for proposal in proposal_list:
                        if proposal.appraisal == appraisal:
                            context['proposal'] = proposal
                            installation_list = Installation.objects.all()
                            if(installation_list):
                                for installation in installation_list:
                                    if installation.proposal == proposal:
                                        context['installation'] = installation
                                        employee_list = Employee.objects.all()
                                        if(employee_list):
                                            for employee in employee_list:
                                                if employee.installation == installation:
                                                    context['employee'] = employee
                                        speakers_list = Speakers.objects.all()
                                        if(speakers_list):
                                            context['speakers_list'] = speakers_list
                                        avcomp_list = AVComponents.objects.all()
                                        if(avcomp_list):
                                            context['avcomp_list'] = avcomp_list
                                        electronics_list = Electronics.objects.all()
                                        if(electronics_list):
                                            context['electronics_list'] = electronics_list
                                        item_list = Item.objects.all()
                                        if(item_list):
                                            for item in item_list:
                                                if item.installation == installation:
                                                    warranty_list = Warranty.objects.all()
                                                    if(warranty_list):
                                                        for warranty in warranty_list:
                                                            if(warranty.item == item):
                                                                installation.total_cost += warranty.cost
                                                    installation.total_labor += item.item_labor_cost
                                                    installation.total_cost += (item.item_cost * item.item_quantity + installation.total_labor)

    return render(request, 'invoices/customer.html', context)

def add_customer(request):
    if request.method=="POST":
        customer = Customer()
        customer.name = request.POST.get('name')
        customer.street = request.POST.get('street')
        customer.city = request.POST.get('city')
        customer.state = request.POST.get('state')
        customer.zipCode = request.POST.get('zipCode')
        customer.phone = request.POST.get('number')
        customer.save()
        return redirect('/')
    else:
        return redirect('/')

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

def add_proposal(request, customer_id):
    if request.method=="POST":
        proposal = Proposal()
        appraisal_list = Appraisal.objects.all()
        if(appraisal_list):
            for appraisal in appraisal_list:
                if appraisal.customer_id == customer_id:
                    proposal.appraisal = appraisal
        proposal.date = request.POST.get('date')
        proposal.description = request.POST.get('description')
        proposal.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

def add_installation(request, customer_id):
    if request.method=="POST":
        customer = get_object_or_404(Customer, pk=customer_id)
        installation = Installation()
        proposal_list = Proposal.objects.all()
        if(proposal_list):
            for proposal in proposal_list:
                if proposal.appraisal.customer_id == customer_id:
                    installation.proposal = proposal
        installation.customer = customer
        installation.date_start = request.POST.get('date_start')
        installation.date_finish = request.POST.get('date_finish')
        installation.description = request.POST.get('description')
        installation.cleanup = request.POST.get('cleanup')
        installation.total_material = request.POST.get('total_material')
        installation.cables_cost = request.POST.get('cables_cost')
        installation.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

def add_employee(request, customer_id):
    if request.method=="POST":
        customer = get_object_or_404(Customer, pk=customer_id)
        employee = Employee()
        installation_list = Installation.objects.all()
        if(installation_list):
            for installation in installation_list:
                if installation.proposal.appraisal.customer_id == customer_id:
                    employee.installation = installation
        employee.name = request.POST.get('name')
        employee.department = request.POST.get('department')
        employee.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

def add_speaker(request, customer_id):
    if request.method=="POST":
        customer = get_object_or_404(Customer, pk=customer_id)
        speakers = Speakers()
        installation_list = Installation.objects.all()
        if(installation_list):
            for installation in installation_list:
                if installation.proposal.appraisal.customer_id == customer_id:
                    speakers.installation = installation
        speakers.item_name = request.POST.get('item_name')
        speakers.item_description = request.POST.get('item_description')
        speakers.item_location = request.POST.get('item_location')
        speakers.item_quantity = request.POST.get('item_quantity')
        speakers.item_cost = request.POST.get('item_cost')
        speakers.item_labor_cost = request.POST.get('item_labor_cost')
        speakers.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

def add_avcomp(request, customer_id):
    if request.method=="POST":
        customer = get_object_or_404(Customer, pk=customer_id)
        avcomp = AVComponents()
        installation_list = Installation.objects.all()
        if(installation_list):
            for installation in installation_list:
                if installation.proposal.appraisal.customer_id == customer_id:
                    avcomp.installation = installation
        avcomp.item_name = request.POST.get('item_name')
        avcomp.item_description = request.POST.get('item_description')
        avcomp.item_location = request.POST.get('item_location')
        avcomp.item_quantity = request.POST.get('item_quantity')
        avcomp.item_cost = request.POST.get('item_cost')
        avcomp.item_labor_cost = request.POST.get('item_labor_cost')
        avcomp.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

def add_electronic(request, customer_id):
    if request.method=="POST":
        customer = get_object_or_404(Customer, pk=customer_id)
        electronic = Electronics()
        installation_list = Installation.objects.all()
        if(installation_list):
            for installation in installation_list:
                if installation.proposal.appraisal.customer_id == customer_id:
                    electronic.installation = installation
        electronic.item_name = request.POST.get('item_name')
        electronic.item_description = request.POST.get('item_description')
        electronic.item_location = request.POST.get('item_location')
        electronic.item_quantity = request.POST.get('item_quantity')
        electronic.item_cost = request.POST.get('item_cost')
        electronic.item_labor_cost = request.POST.get('item_labor_cost')
        electronic.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

def delete_appraisal(request, customer_id):
    if request.method=="POST":
        appraisal_list = Appraisal.objects.all()
        if(appraisal_list):
            for appraisal in appraisal_list:
                if(appraisal.customer_id == customer_id):
                    appraisal.delete()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

def delete_proposal(request, customer_id):
    if request.method=="POST":
        proposal_list = Proposal.objects.all()
        if(proposal_list):
            for proposal in proposal_list:
                if(proposal.appraisal.customer_id == customer_id):
                    proposal.delete()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

def delete_installation(request, customer_id):
    if request.method=="POST":
        installation_list = Installation.objects.all()
        if(installation_list):
            for installation in installation_list:
                if(installation.proposal.appraisal.customer_id == customer_id):
                    installation.delete()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

def delete_employee(request, customer_id):
    if request.method=="POST":
        employee_list = Employee.objects.all()
        if(employee_list):
            for employee in employee_list:
                if(employee.installation.proposal.appraisal.customer_id == customer_id):
                    employee.delete()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

def delete_customer(request, customer_id):
    if request.method=="POST":
        customer = get_object_or_404(Customer, pk=customer_id)
        customer.delete()
        return redirect("/")
    else:
        return redirect("/")

def delete_item(request, item_id):
    if request.method=="POST":
        item = get_object_or_404(Item, pk=item_id)
        customer_id = item.installation.customer_id
        item.delete()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")

def add_warranty(request, item_id):
    if request.method=="POST":
        item = get_object_or_404(Item, pk=item_id)
        customer_id = item.installation.customer_id
        warranty = Warranty()
        warranty.item = item
        warranty.title = request.POST.get('title')
        warranty.start_date = request.POST.get('start_date')
        warranty.mfg_warranty = request.POST.get('mfg_warranty')
        warranty.cost = request.POST.get('cost')
        warranty.save()
        return redirect(f"/invoices/{customer_id}")
    else:
        return redirect(f"/invoices/{customer_id}")


















