from django.shortcuts import render,redirect
from django.http import HttpResponse
from teleapp.models import * 
from django.contrib import messages


# Create your views here.
def index(request):
    persons = Profile.objects.all()

    return render(request,'index.html',{"persons":persons})

def dashboard(request):
    persons = Profile.objects.all()

    return render(request,'dashboard.html',{"persons":persons})

def add_customer(request):
    persons = Profile.objects.all()

    return render(request,'add_customer.html',{"persons":persons})