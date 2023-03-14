"""telesale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from teleapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('', views.index),
    path('register_form/', views.register_form),
    path('login/', views.login,name='login-page'),
    path('dashboard/', views.dashboard,name='dashboard-page'),
    path('add_dashboard/', views.add_dashboard),
    path('add_customer/', views.add_customer),
    

]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT )
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT )