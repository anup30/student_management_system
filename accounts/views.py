from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
    success_message = "Your account was created successfully! You can now log in."