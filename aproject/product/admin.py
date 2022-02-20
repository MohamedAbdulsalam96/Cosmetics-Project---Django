from django.contrib import admin
from .models import Brands
from .models import Products
from .models import Categorys
# Register your models here.
admin.site.register(Brands)
admin.site.register(Products)
admin.site.register(Categorys)
