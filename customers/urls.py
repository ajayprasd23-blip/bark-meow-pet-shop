

from django.urls import path
from . import views

urlpatterns = [
    path('add-customer/', views.add_customer, name='add_customer'),
    path('customers/', views.customer_list, name='customer_list'),
    path('edit-customer/<int:id>/', views.edit_customer, name='edit_customer'),
    path('delete-customer/<int:id>/', views.delete_customer, name='delete_customer'),
]
