from django import forms
from django.core.exceptions import PermissionDenied
from django.http.response import HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic.edit import DeleteView
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from blog.forms import PostForm


def home_view(request):
    print(request.GET)
    q = request.GET.get('q')
    objects = Post.objects.all()
    if q:
        objects = Post.objects.filter(title__contains=q)

    return render(request, 'home.html', {
        'posts': objects,
        'q': q
    })


def post_detail_view(request, pk: int):
    return render(request, 'post-details.html', {
        'post': get_object_or_404(Post, pk=pk)
    })


@login_required(login_url='blog:home')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, user=request.user)

        if not form.is_valid():
             return render(request, 'post-create.html', {
                'form': form
            })
        
        form.save()
        return redirect('blog:home')
    
    return render(request, 'post-create.html', {
        'form': PostForm()
    })

class PostCreateView(CreateView):
    model = Post
    template_name = 'post-create.html'
    form_class = PostForm
    
    def get_success_url(self):
        return reverse('blog:post-details', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs

# class PostDeleteView(DeleteView):
#     model = Post
    



@login_required(login_url='blog:home')
def post_delete(request):
    if request.method != 'POST': 
        return redirect('blog:home')

    post = get_object_or_404(Post, pk=request.POST.get('pk'))
    if post.user != request.user:
        raise PermissionDenied('you are not the owner of this post')

    post.delete()
    return redirect('blog:home')
