from django.db import models




class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    address = models.TextField()

    def __str__(self):
        return self.name


# Create your models here.
