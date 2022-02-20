from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Brands(models.Model):
    Name = models.CharField(max_length=50)
    orgin = models.CharField(max_length=50)
    descreption = models.TextField(default="Lorem Ipsum Dolor Sit Amet, Consectetur Adipisicing Elit. Omnis, Maxime.")
    images = models.ImageField(upload_to='photos/%y/%m/%d', null = True , blank = True)

    def __str__(self):
        return self.Name
############################

class Categorys(models.Model):    # class Category (2)
    Name = models.CharField(max_length=50)
    orgin = models.CharField(max_length=50)
    descreption = models.TextField(default="Lorem Ipsum Dolor Sit Amet, Consectetur Adipisicing Elit. Omnis, Maxime.")
    images = models.ImageField(upload_to='photos/%y/%m/%d', null = True , blank = True)

    def __str__(self):
        return self.Name

############################

class Products(models.Model):
    Name = models.CharField(max_length=50)
    category = models.ForeignKey(Categorys,on_delete=models.CASCADE,  null = True , blank = True)
    descreption = models.TextField(default="Lorem Ipsum Dolor Sit Amet, Consectetur Adipisicing Elit. Omnis, Maxime.")
    Expir_date = models.DateField(default=datetime.now)
    Price = models.IntegerField()
    images = models.ImageField(upload_to='photos/%y/%m/%d', null = True , blank = True)
    brand = models.ForeignKey(Brands,on_delete=models.CASCADE)
#
    def __str__(self):
        return self.Name
#################################3
