from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.brandlist, name='brandlist'),     #brands/
    path('brand',views.brand,name='brand'),         #brands/brand

]