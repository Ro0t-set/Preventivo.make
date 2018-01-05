"""dentisti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from app.models import Cliente
from app.views import home, utente, add_utente, edit_utente, preventivo, add_preventivo, edit_preventivo,stampa_preventivo
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import login, logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('utente/', utente),
    path('add_utente/', add_utente),
    path('utente/<int:pk>/edit/', edit_utente),
    path('preventivo/', preventivo),
    path('add_preventivo/', add_preventivo),
    path('prevetnivo/<int:pk>/edit/', edit_preventivo),
    path('prevetnivo/<int:pk>/stampa/', stampa_preventivo),


]
