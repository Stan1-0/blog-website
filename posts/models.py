from django import forms
from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body =models.CharField(max_length=100000000000)
    post_by = models.CharField(max_length=50, default="Anonymous")
    created_at = models.DateTimeField(default=datetime.now, blank=True)