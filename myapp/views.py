# from django import forms
from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from django.contrib import messages
# from django.contrib.auth import login, logout, authenticate
from django.forms import inlineformset_factory


# from .forms import ImageForm
# from .models import Image

from myapp.models import HelpDesk, House, NewCustomer

# Create your views here.
def index(request):
    context = {
        'variable1':"This is sent",
        'variable2':"Hello"
    }
    return render(request, "index.html", context)

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def register(request):
    return render(request,"register.html")

def gallery(request):
    return render(request,"gallery.html")
    
def home(request):
    return render(request, "home.html")

def helpDesk(request):
    if request.method== "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('description')
        helpDesk1 = HelpDesk(name=name,email=email,desc=desc,date=datetime.today())
        helpDesk1.save()
        messages.success(request,'Your message has been sent.')
    return render(request,"helpDesk.html")

def register(request):
    flag = 0
    if request.method== "POST":
        fname1 = request.POST.get('fname')
        lname1 = request.POST.get('lname')
        dob1 = request.POST.get('dob')
        gender1 = request.POST.get('gender')
        email1 = request.POST.get('email')
        contact1 = request.POST.get('contact')
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        password11 = request.POST.get('password1')

        print(fname1, lname1, dob1, gender1, email1, contact1, username1, password1, password11)

        if not any(char.isdigit() for char in password1):
           messages.success(request, 'No Digits. Register Again')
           flag=1
           return render(request,"register.html")

        if not any(char.isupper() for char in password1):
           messages.success(request, 'Password uppercase. Register Again')
           flag=1
           return render(request,"register.html")
           
        if password1 != password11 :
            messages.success(request, 'Password Mismatch. Register Again')
            flag = 1
            return render(request,"register.html")


        if len(password1) < 6:
            messages.success(request, 'Password must have atleast 6 characters. Register Again')
            flag = 1
            return render(request,"register.html")


        if len(contact1) < 10 or len(contact1) > 10 :
            messages.success(request, 'Mobile Number must be of 10 digits. Register Again')
            flag = 1
            return render(request,"register.html")


        if password1 == password11 and flag == 0:
            newCustomer = NewCustomer(fname=fname1, lname=lname1, dob=dob1, gender=gender1, email=email1, contact=contact1, username=username1, password=password1, password1=password11)
            newCustomer.save()
            messages.success(request,'Registration Successful')
            return render(request,"index.html")


    return render(request,"register.html")

def login(request):

    global logged_in

    new_username = request.POST.get('uname')
    new_password = (request.POST.get('password'))
    
    print(new_username, new_password)
    objects = NewCustomer.objects.all()
    print(objects)

    for object in objects:
        if object.username == new_username and object.password == new_password :
            logged_in = True
            messages.success(request, "Login Successful")
            return render(request, 'home.html')

    messages.warning(request, 'Invalid Credentials')
    return render(request, 'index.html')

def pg(request):
    return render(request, "pg.html")

def rentalHome(request):
    return render(request, "rentalHome.html")

def add(request):
    return render(request, "add.html")

def add_instance(request):
    home_type = request.POST['type']
    bedrooms = request.POST['numberOfBedrooms']
    floor = request.POST['floor']
    lift = request.POST['lift']
    kitchen = request.POST['kitchen']
    bathroom = request.POST['bathroom']
    electricity = request.POST['electricity']
    water = request.POST['water']
    living = request.POST['livingRoom']
    gallery = request.POST['gallery']
    wifi = request.POST['Wifi']
    tv = request.POST['tv']
    pets = request.POST['pets']
    rent = int(request.POST['rent'])
    vacancies = int(request.POST['vacancy'])
    phone = request.POST['phone']
    address = request.POST['address']
    location = request.POST['city']

    instance = House(home_type=home_type, bedrooms=bedrooms, floor=floor, lift=lift, kitchen=kitchen, bathroom=bathroom, electricity=electricity, water=water, living=living, gallery=gallery, wifi=wifi, tv=tv, pets=pets, rent=rent, vacancies=vacancies, phone=phone, address=address, location=location)
    instance.save()
    print("The data is stored in the database")
    messages.success(request, 'Data is stored in our database')
    return render(request, 'home.html')

def search_pg(request):
    vacancies = int(request.POST['vacancy'])
    kitchen = request.POST['kitchen']
    bathroom = request.POST['bathroom']
    electricity = request.POST['electricity']
    water = request.POST['water']
    living = request.POST['livingRoom']
    gallery = request.POST['gallery']
    wifi = request.POST['Wifi']
    tv = request.POST['tv']
    min_rent = int(request.POST['min_rent'])
    max_rent = int(request.POST['max_rent'])
    location = request.POST['city']

    objects = House.objects.all()

    outputs = list()

    for object in objects:
        if object.vacancies<=vacancies and object.kitchen == kitchen and object.bathroom == bathroom and object.electricity == electricity and object.water == water and object.living == living and object.gallery == gallery and object.wifi == wifi and object.tv == tv and min_rent<=object.rent and object.rent<=max_rent and object.location == location:
            outputs.append(object)
    
    return render(request, 'results.html', {'objects': outputs})

def search_house(request):
    bedrooms = int(request.POST['bedrooms'])
    floor = int(request.POST['floor'])
    bathroom = request.POST['bathroom']
    electricity = request.POST['electricity']
    water = request.POST['water']
    gallery = request.POST['gallery']
    lift = request.POST['lift']
    pets = request.POST['pets']
    min_rent = int(request.POST['min_rent'])
    max_rent = int(request.POST['max_rent'])
    location = request.POST['city']

    objects = House.objects.all()

    outputs = list()

    for object in objects:
        if int(object.bedrooms)>=bedrooms and int(object.floor) <= floor and object.bathroom == bathroom and object.electricity == electricity and object.water == water and object.gallery == gallery and object.pets==pets and object.lift==lift and min_rent<=object.rent and object.rent<=max_rent and object.location == location:
            outputs.append(object)
    
    return render(request, 'results.html', {'objects': outputs})
