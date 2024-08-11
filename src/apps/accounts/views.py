from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/homepage')
        else:
            return HttpResponse("Ungültige Anmeldedaten")
    return render(request, 'accounts/login.html', {'app_style': "app-styles/accounts.css"})


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Benutzername ist bereits vergeben.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'E-Mail ist bereits registriert.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                login(request, user)
                return redirect('/homepage') 
        else:
            messages.error(request, 'Passwörter stimmen nicht überein.')
    
    return render(request, 'accounts/register.html', {
        'app_style': "app-styles/accounts.css",
        })


@login_required
def homepage_view(request):
    username = request.user.username
    return render(request, 'homepage.html', {
        'app_style': "app-styles/homepage.css",
        "username": username
        })
