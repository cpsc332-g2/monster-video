from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:customer_id>/', views.details, name='details'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('<int:customer_id>/add_appraisal/', views.add_appraisal, name='add_appraisal'),
    path('<int:customer_id>/add_proposal/', views.add_proposal, name='add_proposal'),
    path('<int:customer_id>/add_installation/', views.add_installation, name='add_installation'),
    path('<int:customer_id>/add_employee/', views.add_employee, name='add_employee'),
    path('<int:customer_id>/add_speaker/', views.add_speaker, name='add_speaker'),
    path('<int:customer_id>/add_avcomp/', views.add_avcomp, name='add_avcomp'),
    path('<int:customer_id>/add_electronic/', views.add_electronic, name='add_electronic'),
    path('<int:customer_id>/delete_appraisal/', views.delete_appraisal, name='delete_appraisal'),
    path('<int:customer_id>/delete_proposal/', views.delete_proposal, name='delete_proposal'),
    path('<int:customer_id>/delete_installation/', views.delete_installation, name='delete_installation'),
    path('<int:customer_id>/delete_employee/', views.delete_employee, name='delete_employee'),
    path('<int:customer_id>/delete_customer/', views.delete_customer, name='delete_customer'),
    path('<int:item_id>/delete_item/', views.delete_item, name='delete_item'),
    path('<int:item_id>/add_warranty/', views.add_warranty, name='add_warranty'),
]