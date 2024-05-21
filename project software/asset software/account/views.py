
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

# Create your views here.

def Login(request):
    return render(request, 'login.html')


def CreateStaff(request):
    
    if request.method == 'POST':
        username = request.POST['uname']
        phone_number = request.POST['number']
        othername = request.POST['oname']
        department = request.POST['department']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if Users.objects.filter(username=username).exists():
                messages.info(request, 'Username is Taken')
                return redirect('createStaff')
            else:
                Users.objects.create(
                    username = username,
                    phone_number = phone_number,
                    first_name = othername,
                    department = department,
                    password = password
                )
                messages.success(request, f'{username} Account Was Created Successfully, Log in Here')
                return redirect('dashboard')
        else:
            messages.info(request, 'The two Password did not match, please try again')
            return redirect('createStaff')
    return render(request, 'newstaff.html')
