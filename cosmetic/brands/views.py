from django.shortcuts import render

# Create your views here.
def brandlist(request):
    return render(request,'brands/brandlist.html')

def brand(request):
    return render(request,'brands/brand.html')