from django.db import models

# Create your models here.
from django.urls import reverse

class book_detail(models.Model):
    Book_name=models.CharField(max_length=120)
    Author=models.CharField(max_length=130)
    genre=models.CharField(max_length=123)
    language=models.CharField(max_length=123)