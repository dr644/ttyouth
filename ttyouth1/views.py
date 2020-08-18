from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from os.path import join
from django.conf import settings



# Create your views here.

def home(request):
    return render(request, 'ttyouth1/home.html')

def photos(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + "/ttyouth1/images/")
    context = {"images": img_list}
    return render (request, 'ttyouth1/photos.html', context)

def sponsors(request):
    return render(request, 'ttyouth1/sponsors.html')