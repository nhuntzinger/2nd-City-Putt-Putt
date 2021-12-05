import datetime
import django
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from .models import Profile, PlayerInfo, DrinkInfo, DrinkOrder, VenueInfo, Tournament
from .logic import *
from django.urls import reverse
from .forms import DrinkForm, TournamentForm

@csrf_protect
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
            location = determine_redirect_login(user)
            print(location)
            return redirect(location)
        else:
            messages.error(request,'username or password not correct')

    return render(request,
    'registration/login.html'
    )

def homeFunc(request):
    user = request.user
    location = determine_redirect_login(user)
    return redirect(location)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
    
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            profile_creation(user=user)
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
    all_members = User.objects.all()

    profile = None
    player_info = None

    tournament = None
    done = None
    if request.user.is_authenticated:
        info = get_player(request.user)
        game_info = get_game_info(request.user)
        hole = game_info['current_hole']
        profile = info['profile']
        player_info = info['player_info']
        tournament = player_info.tournament
        if hole >= get_number_of_holes():
            done = True

    else:
        print('no authorized user')

    #if profile != None and player_info != None:
        #tournament_for_player(player_info)

    context = {'all': all_members, 'profile': profile, 'player_info' : player_info, 'tournament' : tournament, 'game_done': done}

    return render(request,
    'puttputt/index.html',
    context)

def order(request):
    all_drinks = DrinkInfo.objects.all
    info = get_player(request.user)
    player_info = info['player_info']
    context = {'drinks': all_drinks, 'player_info': player_info}
    return render(request, 'puttputt/order.html', context)


def order_drink(request):
    user = request.user
    drink = request.POST.get('drink')
    quantity = request.POST.get('qty')
    info = get_player(user)
    player_info = info['player_info']
    player_info.current_funds -= int(request.POST.get('total'))
    player_info.save()
    new_order = DrinkOrder(drink=DrinkInfo.objects.get(title=drink), user=user, order_delivered=False, quantity=quantity)
    user.save()
    new_order.save()

    return redirect('game')

def add_funds(request):
    info = get_player(request.user)
    funds = request.POST.get('funds')
    player_info = info['player_info']
    player_info.current_funds += int(funds)
    player_info.save()
    return redirect('order')

def logout_request(request):
    logout(request)
    return redirect("index")

# the main game 
def game(request):
    game_info = get_game_info(request.user)
    active_drinks = DrinkOrder.objects.filter(user=request.user, order_delivered=False)
    if active_drinks.count() == 0:
        active_drinks = None

    score = game_info['current_score']
    hole = game_info['current_hole']

    last_hole = hole == VenueInfo.objects.all()[:1].get().number_of_holes

    context = {'score': score, 'hole': hole, 'last_hole': last_hole, 'drinks':active_drinks}

    return render(request, 'puttputt/game.html', context)

def add_stroke(request):
    """this function serves the purpose of eating game stroke submissions
    then redirecting back to the game board so they can't accidentally refresh
    then submit again
    """
    print('adding a stroke')
    stroke = request.POST['button']

    player = get_player(request.user)

    location = add_stroke_to_player(player, stroke)

    # need to check if they need to go to the final page since they just did the last hole!
    return redirect(location)


def barista(request):
    """The barista's dashboard"""
    drinks_outstanding = DrinkOrder.objects.filter(order_delivered=False)

    # this is so we can know in the template not to render the list
    if drinks_outstanding.count() == 0:
        drinks_outstanding = None

    context = {'drinks': drinks_outstanding}

    return render(request, 'puttputt/barista.html', context)

def manager(request):
    """The manager's dashboard"""
    all_users = User.objects.all

    context = {'all_users': all_users}

    return render(request, 'puttputt/manager.html', context)

def sponsor(request):
    """The sponsor's dashboard"""

    spons = get_sponsor(request.user)

    tournament = tournament_for_sponsor(spons)

    form = TournamentForm()

    players_in_tournament = PlayerInfo.objects.filter(tournament=tournament)

    players_without_tournaments = PlayerInfo.objects.filter(tournament=None)

    context = {'tournament': tournament, 'form': form, 'players': players_without_tournaments, 'playerz': players_in_tournament}

    return render(request, 'puttputt/sponsor.html', context)

def sponsor_date(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TournamentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # todo 

            start_time = form.cleaned_data['start_time']
            print(start_time)
            register_tournament_on_date(request.user, start_time)
            return redirect('sponsor')

    # if a GET (or any other method) we'll create a blank form
    else:
        return redirect('sponsor')

def sponsor_pay_fee(request):
    pay_fee_for_sponsor(request.user)

    return redirect('sponsor')

def sponsor_add_player(request):
    player_username = request.POST['button']

    add_player_to_sponsor(request.user, player_username)

    return redirect('sponsor')

def edit_user(request):

    username = request.GET['username']

    profile_type = get_user_current_type(username)

    context = {'username': username, 'current': profile_type}

    return render(request, 'puttputt/edit_user.html', context)

def end_game(request):
    score = get_final_score(request.user)

    # todo: get their CURRENT place on the leaderboard among the other players that are in the same tournament
    # todo: maybe also mention that their game is not yet complete so they cannot claim a prize yet, they will have to wait for the other players

    # gets the leaderboard for their tournament
    leaderboard = get_leaderboard_for(request.user)

    is_game_complete = check_game_complete_for(request.user)

    context = {'leaderboard': leaderboard, 'is_game_complete': is_game_complete}

    context = {'score': score}

    return render(request, 'puttputt/end_game.html', context)

def register_tournament_on_date(user, start_time):
    sponsor = get_sponsor(user)
    
    # right now there is no logic that prevents them fron adding a ton of tournaments on the same day so good luck
    tournament = Tournament.objects.create(
        sponsor=sponsor,
        start_time=start_time,
        end_time=start_time + datetime.timedelta(days=1), # tournaments are 1 day in length
        fee_paid=False
    )

    return tournament

def leaderboard(request):
    leaderboard = get_all_time_leaderboard()

    player_score = get_final_score(request.user)

    context = {'leaderboard': leaderboard, 'player_score': player_score}

    return render(request, 'puttputt/leaderboard.html', context)

def change_user_type(request):
    if 'player' in request.POST:
        username = request.POST['player']
        set_user_type('player', username)
    elif 'sponsor' in request.POST:
        username = request.POST['sponsor']
        set_user_type('sponsor', username)
    elif 'manager' in request.POST:
        username = request.POST['manager']
        set_user_type('manager', username)
    else:
        username = request.POST['barista']
        set_user_type('barista', username)

    return redirect(manager)

def edit_drink_menu(request):
    current_drink_options = DrinkInfo.objects.all()
    context = {"current_drink_options": current_drink_options}

    return render(request, 'puttputt/edit_drink_menu.html', context)

def add_drink(request):
    if request.method == "POST":
        form = DrinkForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            if image == '':
                drink = DrinkInfo(title=title, price=price)
                drink.save()
            else:
                drink = DrinkInfo(title=title, price=price, image=image)
                drink.save()

        else:
            messages.error(request, 'please enter a drink name and drink price')
    else:
        form = DrinkForm()


    return redirect(edit_drink_menu)

def remove_drink(request, pk):
    drink = get_object_or_404(DrinkInfo, pk=pk)

    if request.method == "POST":
        drink.delete()

    return redirect(edit_drink_menu)

def mark_delivered(request, pk):
    drink = get_object_or_404(DrinkOrder, pk=pk)
    if request.method == "POST":
        drink.order_delivered = True
        drink.save()

    return redirect(barista)

