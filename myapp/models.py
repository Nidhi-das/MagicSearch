from django.db import models
# from django import forms

# Create your models here.
class House(models.Model):
    home_type = models.CharField(max_length=5)
    bedrooms = models.CharField(max_length=3)
    floor = models.CharField(max_length=3)
    lift = models.CharField(max_length=4)
    kitchen = models.CharField(max_length=4)
    bathroom = models.CharField(max_length=4)
    electricity = models.CharField(max_length=4)
    water = models.CharField(max_length=4)
    living = models.CharField(max_length=4)
    gallery = models.CharField(max_length=4)
    wifi = models.CharField(max_length=4)
    tv = models.CharField(max_length=4)
    pets = models.CharField(max_length=4)
    rent = models.IntegerField()
    vacancies = models.IntegerField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    location = models.CharField(max_length=10)
    
    def __str__(self):
        return self.home_type



class HelpDesk(models.Model):
    name= models.CharField(max_length=20)
    email= models.CharField(max_length=30)
    desc= models.TextField()
    date= models.DateField()
    def __str__(self):
        return self.name

# class RegisteredCustomer(models.Model):
#     username= models.CharField(max_length=20)
#     password= models.CharField(max_length=20)

class NewCustomer(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    password1 = models.CharField(max_length=20)
