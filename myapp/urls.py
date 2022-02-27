from django.contrib import admin
from django.urls import path, include
from myapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path("gallery",views.gallery,name='gallery'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("helpDesk",views.helpDesk,name='helpDesk'),
    path("pg",views.pg,name='pg'),
    path("rentalHome",views.rentalHome,name='rentalHome'),
    path ("search_pg", views.search_pg, name='search_pg'),
    path ("search_house", views.search_house, name='search_house'),
    path("add", views.add, name='add'),
    path ("add_instance", views.add_instance, name='add_instance'),
    path("login",views.login,name='login'),
    path("home", views.home, name="home"),
    path("register",views.register,name='register'),
]