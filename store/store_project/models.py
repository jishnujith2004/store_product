from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=15)
    description=models.TextField()
    category=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    stock=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)