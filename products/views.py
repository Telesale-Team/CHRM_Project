from django.shortcuts import render

# Create your views here.


def product(request):
    x = 1 
    return render(request,'teleapp/index.html')