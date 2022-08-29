from django.db import models

class APIModel(models.Model):

    name=models.CharField(max_length=10)
    age=models.IntegerField()
    location=models.CharField(max_length=10)