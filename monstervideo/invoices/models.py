from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=80)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=15)
    zipCode = models.IntegerField()
    phone = models.IntegerField()

class Appraisal(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)

    location = models.CharField(max_length=20)
    #maxSize = models.IntegerField()
    cableRun = models.BooleanField(default=False)
    comments = models.CharField(max_length=150)

class Proposal(models.Model):
    appraisal = models.ForeignKey(Appraisal, on_delete = models.CASCADE)

    date = models.DateField(auto_now=False, auto_now_add=True)
    description = models.CharField(max_length=200)

class Warranty(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)

    start_date = models.DateField(auto_now=False, auto_now_add=True)
    title = models.CharField(max_length=30)
    mfg_warranty = models.IntegerField(default=2)  #mfg_warranty is manufacturer warranty
    add_warranty = models.IntegerField(default=0)
    #coverage = models.BooleanField()
    cost = models.FloatField(default=0.0)

class Installation(models.Model):
    proposal = models.ForeignKey(Proposal, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)

    date_start = models.DateField(auto_now=False, auto_now_add=True)
    date_finish = models.DateField(auto_now=False, auto_now_add=False)
    cleanup = models.BooleanField(default=False)
    total_material = models.FloatField(default=0.0)
    total_labor = models.FloatField(default=0.0)
    total_cost = models.FloatField(default=0.0)
    cables_cost = models.FloatField(default=0.0)

class Employee(models.Model):
    installation = models.ForeignKey(Installation, on_delete = models.CASCADE)

    name = models.CharField(max_length=40)
    department = models.CharField(max_length=40)

class Speakers(models.Model):
    installation = models.ForeignKey(Installation, on_delete = models.CASCADE)

    location = models.CharField(max_length=80)
    cost = models.FloatField(default=0.0)
    labor = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)

class AVComponents(models.Model):
    installation = models.ForeignKey(Installation, on_delete = models.CASCADE)

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=80)
    sale = models.FloatField(default=0.0)
    salesprice = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    subtotal = models.FloatField(default=0.0)

class Electronics(models.Model):
    installation = models.ForeignKey(Installation, on_delete = models.CASCADE)

    labor = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)

class Item(models.Model):
    installation = models.ForeignKey(Installation, on_delete = models.CASCADE)
    warranty = models.OneToOneField(Warranty, on_delete = models.CASCADE)

    item_category = models.CharField(max_length=15,default="AVComponents")
    item_name = models.CharField(max_length=30)
    item_cost = models.FloatField(default=0.0)
    item_quanity = models.IntegerField()