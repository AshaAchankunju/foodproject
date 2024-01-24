from django.db import models

# Create your models here.
from django.db import models

class Food(models.Model):
    name=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    color=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    price=models.IntegerField()

    def __str__(self) :
        return self.name








