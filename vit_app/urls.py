from django.contrib import admin
from django.urls import path, include
from vit_app import views

urlpatterns = [
    path('',views.index,name=''),
    path('login',views.login,name='login'),
    path('register',views.register,name='register')
]