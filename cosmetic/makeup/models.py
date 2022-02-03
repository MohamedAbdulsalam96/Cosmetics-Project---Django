from django.db import models
# from brands.models import Brand
from datetime import datetime
# Create your models here.
class Brand (models.Model):
    # brand_id = models.name = models.ForeignKey('TargetModel', related_name='', on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    orgin = models.CharField(max_length=50)
    images = models.ImageField(null = True , blank = True)

    def __str__(self):
        return self.Name


class Product(models.Model):
    Name = models.CharField(max_length=50)
    kind = models.CharField(max_length=20)
    descreption = models.TextField(default="none")
    Expir_date = models.DateField(default=datetime.now)
    Price = models.IntegerField()
    images = models.ImageField(null = True , blank = True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
#
    def __str__(self):
        return self.Name



# class Categorys(models.Model):    # class Category (2)
#     Name = models.CharField(max_length=50)
#     orgin = models.CharField(max_length=50)
    # images = models.ImageField()


    # img = models.ImageField(upload_to='photos/%y/%m/%d', default='')






  