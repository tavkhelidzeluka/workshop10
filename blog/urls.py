from django.urls import path
from blog.views import PostCreateView, PostDeleteView, home_view, post_create, post_delete, post_detail_view, \
    PostListView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', post_detail_view, name='post-details'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/create/', PostCreateView.as_view(), name='post-create')
]
