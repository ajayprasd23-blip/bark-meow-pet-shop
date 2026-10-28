

from django.shortcuts import render, redirect,get_object_or_404
from .forms import CustomerForm
from .models import Customer


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()

    return render(request, 'customers/add_customer.html', {
        'form': form
    })


def customer_list(request):
    customers = Customer.objects.all()

    return render(request, 'customers/customer_list.html', {
        'customers': customers
    })


# Create your views here.

def edit_customer(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'customers/edit_customer.html', {
        'form': form,
        'customer': customer
    })

def delete_customer(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')

    return render(request, 'customers/delete_customer.html', {
        'customer': customer
    })
