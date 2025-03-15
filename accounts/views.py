from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.shortcuts import render

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
    success_message = "Your account was created successfully! You can now log in."
    


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)

def logout_view(request):
    logout(request)  # for eg. keep the session for storing other information like user preferences or shopping cart data.
    # request.session.flush()  # completely clear the session data and delete the session cookie. logout.
    return redirect("home")