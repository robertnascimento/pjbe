"""bestcars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path 
from core.views import caduser, bestcars , motos, carros, users, cadcar, cadmoto

urlpatterns = [
    path('carros/',carros, name='carros'),
    path('cadcar/',cadcar, name='cadcar'),
    path('cadmoto/',cadmoto, name='cadmoto'),
    path('users/',users, name='users'),
    path('caduser/',caduser, name='caduser'),
    path('motos/',motos, name='motos'),
    path('bestcars/',bestcars, name='bestcars'),
    path('admin/', admin.site.urls),
]
