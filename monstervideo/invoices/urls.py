from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:customer_id>/', views.details, name='details'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('<int:customer_id>/add_appraisal/', views.add_appraisal, name='add_appraisal'),
]