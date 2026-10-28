

from django.urls import path
from . import views

urlpatterns = [
    path('add-pet/', views.add_pet, name='add_pet'),
    path('pets/', views.pet_list, name='pet_list'),
    path('edit-pet/<int:id>/', views.edit_pet, name='edit_pet'),
    path('delete-pet/<int:id>/', views.delete_pet, name='delete_pet'),
]
