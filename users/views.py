from dataclasses import field
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from users.forms import UserCreationForm
from users.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')

    def get(self, request, *args: str, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog:home')
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args: str, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog:home')
        return super().post(request, *args, **kwargs)
    
    def get_success_message(self, cleaned_data) -> str:
        return f'{self.object.username} successfully created!'