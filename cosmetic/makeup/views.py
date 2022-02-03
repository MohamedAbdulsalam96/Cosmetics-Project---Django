from django import views
from django.shortcuts import render
from .models import Product, Brand
# Create your views here.
     ### Homes Page.. (index.html)
def index(request):
    return render(request,'makeup/index.html')
    #################################
    ### Brands Pages
def brandlist(request):         # Brands list....
    context= {'brand': Brand.objects.all()}
    return render(request,'makeup/brand/brands.html',context)

def brand(request,brandName):   # Brand Details....
    return render(request,'makeup/brand/brand.html', {'brand1': Brand.objects.get(Name=brandName)})

    #################################
    ###Products Pages
def products(request):          # Products Lists....
    context= {'pro': Product.objects.all()}
    return render(request,'makeup/product/products.html',context)

def product(request,proName):   # Product Details....   
    # context= {'pro': Product.objects.get(proName)}
    return render(request,'makeup/product/product.html',{'pro1': Product.objects.get(Name=proName)})







 