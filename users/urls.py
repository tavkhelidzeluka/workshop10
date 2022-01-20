from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from users.views import RegisterView


app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(next_page=reverse_lazy('blog:home'), redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('users:login')), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
