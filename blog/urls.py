from django.urls import path
from blog.views import PostCreateView, home_view, post_create, post_delete, post_detail_view


app_name = 'blog'

urlpatterns = [
    path('', home_view, name='home'),
    path('post/<int:pk>/', post_detail_view, name='post-details'),
    path('post/delete/', post_delete, name='post-delete'),
    path('post/create/', PostCreateView.as_view(), name='post-create')
]
