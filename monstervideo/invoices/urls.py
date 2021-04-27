from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:customer_id>/', views.details, name='details'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('<int:customer_id>/add_appraisal/', views.add_appraisal, name='add_appraisal'),
    #To-do
    path('<int:customer_id>/add_proposal/', views.add_proposal, name='add_proposal'),
    path('<int:customer_id>/add_installation/', views.add_installation, name='add_installation'),
    path('<int:customer_id>/add_employee/', views.add_employee, name='add_employee'),
    path('<int:customer_id>/add_item/', views.add_item, name='add_item'),
    path('<int:customer_id>/add_speaker/', views.add_speaker, name='add_speaker'),
    path('<int:customer_id>/add_avcomponents/', views.add_avcomponents, name='add_avcomponents'),
    path('<int:customer_id>/add_electronics/', views.add_electronics, name='add_electronics'),
    path('<int:customer_id>/add_warranty/', views.add_warranty, name='add_warranty'),

    

]
