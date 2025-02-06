from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=200, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    
    def __str__ (self):
        return self.first_name +"   "+ self.last_name

