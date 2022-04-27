from contextlib import nullcontext
from email.mime import image
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null= True)
    image = models.ImageField(upload_to='article/', null=False)
    created_at = models.DateField(auto_now_add=True, null=True)
