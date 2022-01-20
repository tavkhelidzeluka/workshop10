from django.db import models
from django.urls import reverse

from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    body = models.TextField()

    background_image = models.ImageField(upload_to='posts/')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog:post-details', kwargs={"pk": self.pk})
    