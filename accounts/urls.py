from django.urls import path
from .views import RegisterView, LoginView, LogoutView #login_view, logout_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
	path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
	#path('login/', login_view, name="login"),
	#path('logout/', logout_view, name="logout"),
]