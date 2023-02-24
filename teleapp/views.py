from django.shortcuts import render,redirect
from django.http import HttpResponse
from teleapp.models import * 
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import datetime


# Create your views here.
def index(request):
    persons = Profile.objects.all()

    return render(request,'index.html',{"persons":persons})

def login(request):
    persons = Profile.objects.all()
    return render(request,'login.html',{"persons":persons})


def dashboard(request):
    persons = TeamStat.objects.all()
    return render(request,'dashboard.html',{"persons":persons})


def add_customer(request):
    persons = Profile.objects.all()
    return render(request,'add_customer.html',{"persons":persons})


def register_form(request):
    persons = Profile.objects.all()
    return render(request,'register_form.html',{"persons":persons})


def add_dashboard(request):
    persons = TeamStat.objects.all()
    return render(request,'add_dashboard.html',{"persons":persons})