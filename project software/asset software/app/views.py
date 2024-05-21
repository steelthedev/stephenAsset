
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from account.models import Users
from django.contrib.auth.decorators import login_required

# Create your views here.

def Home(request):
    return render(request, 'index.html')


def Dashboard(request):
    user = request.user
    users = Users.objects.all()
    context = {
        'user': user,
        'users': users,
    }
    return render(request, 'dashboard.html', context)


def Asset(request):
    return render(request, 'asset.html')


def Staffs(request):
    users = Users.objects.all().order_by('-id')
    context = {
        'users': users,
    }
    return render(request, 'staffs.html', context)


def AddAsset(request):
    users = Users.objects.all()
    if request.method == 'POST':
        assetName = request.POST['name']
        user = request.POST['user']
        
    context = {
        'users': users,
    }
    return render(request, 'newItem.html', context)



