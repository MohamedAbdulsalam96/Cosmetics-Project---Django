from operator import mod
from statistics import mode
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=20)
    descreption = models.TextField()
    Expir_date = models.DateField()
    Price = models.IntegerField()

    def __str__(self):
        return self.name

     