from django.shortcuts import redirect, render
from .models import Products, Brands, Categorys
from django.db.models import Q
from email import message
from itertools import count
from multiprocessing import context
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
import datetime



# Create your views here.

def home(request):
    pro = Products.objects.all()
    brand =  Brands.objects.all()
    cate = Categorys.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    product_list = Products.objects.all()
    pro_set =  Products.objects.filter(
             Q(category__Name__icontains = q) |
             Q(Name__icontains = q)).order_by('-id')  
    context = {"prolist": product_list,
               "proSet": pro_set,
               "pro":pro,
               "brand":brand,
               "cate":cate}
    return render(request,'home.html',context)


   


def product_page(request):
    pro = Products.objects.all()
    brand =  Brands.objects.all()
    cate = Categorys.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    product_list = Products.objects.all()
    pro_set =  Products.objects.filter(
             Q(category__Name__icontains = q) |
             Q(Name__icontains = q)).order_by('-id')  
    context = {"prolist": product_list,
               "proSet": pro_set,
               "pro":pro,
               "brand":brand,
               "cate":cate}
    return render(request,'product/product_page.html', context)


def product(request,proName):
    product_item = Products.objects.get(id=proName)
    Related = Products.objects.filter(category=product_item.category)
    pro = Products.objects.all()
    context = {"pro_item":product_item,
                "pro": pro,
                "Related":Related}
    return render(request,'product/product.html',context)

def Categorylist(request,cateName):
    cate_item = Categorys.objects.getall()
    context = {"cate":cate_item}
    return render(request,'category/category.html', context)


def Category(request,cateName):
    cate_item = Categorys.objects.get(id=cateName)
    context = {"cate_item":cate_item}
    return render(request,'category/category.html', context)


# def creat_connect(request):
#     form = connect_us_form()
#     if request.method == "POST":
#         form = connect_us_form(request.POST) 
#         if form.is_valid():
#             form.save()
#             return redirect('home')

#     context = {'form' : form}
#     return render(request, 'makeup/connect_us.html',context)


def loginPage(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist ')

        user = authenticate(request, username=username, password = password)

        # if user is not None:
        #     login(request,user)
        #     return redirect('home')
        # else:
        #     messages.error(request, 'Username or password not exist ')
    context = {'page': page}
    return render(request, 'login_regester.html', context)
def logoutUser(requset):
    logout(requset)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
         
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'An error in registeration ')
    context = {'page': page, 'form':form}
    return render(request, 'login_regester.html', context)

