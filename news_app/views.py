from django.shortcuts import render
from .forms import CustomeUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.


class SingUpView(CreateView):
    form_class = CustomeUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/singup.html'
