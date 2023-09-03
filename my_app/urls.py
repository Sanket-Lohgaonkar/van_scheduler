from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('',views.main, name='main'),
    path('select_timing/', views.select_timing, name='select_timing'),
    path('about_us/', views.about_us, name='about_us'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
    path('register/', views.Register, name='Register'),
    path('services/', views.services, name='services'),
    path('Admin_Login/', views.Admin_Login, name='Admin_Login'),
    path('Admin_window/', views.Admin_window, name='Admin_window'),
    path('loginex/', views.loginex, name='loginex'),
]
