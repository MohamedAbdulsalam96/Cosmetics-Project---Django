from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('product/product/<str:proName>', views.product, name ='product'),
    path('product/product_page', views.product_page, name ='product_page'),
    # path('category/<str:cateName>', views.Category, name ='category'),
    path('login/', views.loginPage, name ='login'),
    path('register/', views.registerPage, name ='register'),


    
]




