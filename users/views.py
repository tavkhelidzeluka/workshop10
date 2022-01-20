from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.views.generic import CreateView
from users.forms import UserCreationForm

from users.models import User
from django.urls import reverse_lazy


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')

