from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, FormView, View
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.shortcuts import render

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
    success_message = "Your account was created successfully! You can now log in."
    
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.contrib.auth.forms import AuthenticationForm

"""
# works, elegent way.
class LoginView(AuthLoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
"""

from django.contrib.auth import login, logout
# simpler
class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        # request.session.flush()  # completely clear the session data and delete the session cookie
        return redirect('home')


"""
# more elegent way, but getting HTTP ERROR 405 here, as trying to acces URL with a method (like GET) that the view doesn't support.
class LogoutView(AuthLogoutView):
    next_page = reverse_lazy('home')
    #http_method_names = ['get', 'post']  # to fix, Allow both GET and POST methods or Create a logout form that uses POST (more secure)
"""    


"""
# function based views:
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
    
"""