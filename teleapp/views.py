from django.shortcuts import render,redirect
from django.http import HttpResponse
from teleapp.models import * 
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')


def dashboard(request):
    team = Product.objects.all()
    expense = expenses.objects.all()
  
    current_datetime = timezone.now()
    time = current_datetime.strftime('%d-%m-%Y')
    return render(request,'dashboard.html',{"team":team,"time":time,"expense":expense})


def Expense(request):
    user = User.objects.all()
    expense = expenses.objects.all()

    
  
   
    return render(request,'dashboard.html',{"user":user,"time":time,"expense":expense})

def add_customer(request):
    persons = Profile.objects.all()
    return render(request,'add_customer.html',{"persons":persons})


def register_form(request):
    persons = Profile.objects.all()
    return render(request,'register_form.html',{"persons":persons})


def add_dashboard(request):
    persons = Team.objects.all()
    return render(request,'add_dashboard.html',{"persons":persons})