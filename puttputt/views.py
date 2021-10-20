from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from puttputt.models import Profile

def login(request):
    return render(request,
    'puttputt/login.html'
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
        form = UserCreationForm()

    context = {'form': form}
    return render(request,
    'registration/register.html',
    context
    )

def index(request):
    all_members = User.objects.all

    return render(request,
    'puttputt/index.html',
    {'all': all_members}
)

