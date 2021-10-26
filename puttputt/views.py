from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from puttputt.models import Profile

def login(request):
    return render(request,
    'puttputt/index.html'
    )


def register(request):

    global error
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    
        if form.is_valid():
            error = "<h1> nah we good </h1>"
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return HttpResponseRedirect('index')

    else:
        error = '<h1> There was an error </h1>'
        form = UserCreationForm()

    context = {'form': form, 'error': error}
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

