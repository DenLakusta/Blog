from django.shortcuts import render
from .models import Contact
from django.views.generic import CreateView
from .forms import ContactForm
# Create your views here.



class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    # success_url = "/"

