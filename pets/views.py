
from django.shortcuts import render, redirect,get_object_or_404
from .models import Pet
from .forms import PetForm


def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()

    return render(request, 'pets/add_pet.html', {
        'form': form
    })


def pet_list(request):
    pets = Pet.objects.all()

    return render(request, 'pets/pet_list.html', {
        'pets': pets
    })


# Create your views here.

def edit_pet(request, id):
    pet = get_object_or_404(Pet, id=id)

    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)

        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)

    return render(request, 'pets/edit_pet.html', {
        'form': form,
        'pet': pet
    })

def delete_pet(request, id):
    pet = get_object_or_404(Pet, id=id)

    if request.method == 'POST':
        pet.delete()
        return redirect('pet_list')

    return render(request, 'pets/delete_pet.html', {
        'pet': pet
    })
