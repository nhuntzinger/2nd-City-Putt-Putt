"""puttputt URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('login', views.loginFunc, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_request, name='logout_request'),
    path('game', views.game, name='game'),
    path('barista', views.barista, name='barista'),
    path('manager', views.manager, name='manager'),
    path('sponsor', views.sponsor, name='sponsor'),
    path('edit_user', views.edit_user, name='edit_user'),
    path('add-stroke', views.add_stroke, name='add-stroke'),
    path('end_game', views.end_game, name='end_game'),
    path('sponsor_date', views.sponsor_date, name='sponsor_date'),
    path('sponsor_pay_fee', views.sponsor_pay_fee, name='sponsor_pay_fee'),
    path('sponsor_add_player', views.sponsor_add_player, name='sponsor_add_player'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
]
