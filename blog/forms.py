from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        post = super().save(commit=False)
        post.user = self.user

        if commit:
            post.save()

        return post


    class Meta:
        model = Post
        exclude = ['user']
