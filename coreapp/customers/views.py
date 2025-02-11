from django.shortcuts import render
from .forms import CustomerRegistrationForm

# Create your views here.
def Registration(request):
    form = CustomerRegistrationForm()
    return render(request, 'customers/customer-registration.html')
