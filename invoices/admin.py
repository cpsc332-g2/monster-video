from django.contrib import admin

from .models import Customer, Appraisal, Proposal, Warranty, Installation, Employee, Speakers, AVComponents, Electronics, Item

admin.site.register(Customer)
admin.site.register(Appraisal)
admin.site.register(Proposal)
admin.site.register(Warranty)
admin.site.register(Installation)
admin.site.register(Employee)
admin.site.register(Speakers)
admin.site.register(AVComponents)
admin.site.register(Electronics)
admin.site.register(Item)
