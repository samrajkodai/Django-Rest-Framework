from django.db import models

# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=20)
    content=models.CharField(max_length=30)
    price=models.IntegerField(max_length=20)
    