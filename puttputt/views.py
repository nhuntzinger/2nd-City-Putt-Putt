import django
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages

from puttputt.models import Profile

def loginFunc(request):
    if request.method == 'POST':
        print(request.POST['username'])
        print(request.POST['password'])
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print('user found')
            return redirect('index')
        else:
            messages.error(request,'username or password not correct')

    return render(request,
    'registration/login.html'
    )


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
    
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()

    context = {'form': form}
    # might want to use HttpResponseRedirect here so user doesn't resubmit data if they hit the back button
    return render(request,
    'registration/signup.html',
    context
    )

def index(request):
    all_members = User.objects.all

    return render(request,
    'puttputt/index.html',
    {'all': all_members}
)

def logout_request(request):
    logout(request)
    return redirect("index")

