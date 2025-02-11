from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.Form):
    first_name = forms.CharField(required=True, label= "Enter first name")
    last_name = forms.CharField(required=True, label= "Enter last name")
    email = forms.EmailField(required=True, widget=forms.EmailInput, label= "Enter email address")
    phone_number = forms.CharField(required=True, label= "Enter phone number")
    address = forms.CharField(required=True, label= "Enter delivery address")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label= "Enter password")

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'password']