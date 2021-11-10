from puttputt.models import *

def profile_creation(user):
    profile = Profile.objects.create(user=user)
    profile.save()
    playerInfo = PlayerInfo.objects.create(profile=profile)
    profile.save()

def get_player(user):
    profile = None
    player_info = None
    try:
        profile = Profile.objects.get(user=user)
        player_info = PlayerInfo.objects.get(profile=profile)
    except:
        print("player not found!")

    return {'profile': profile, 'player_info': player_info}

def get_sponsor(user):
    try:
        profile = Profile.objects.get(user=user)
        sponsor = SponsorInfo.objects.get(profile=profile)
        return sponsor
    except:
        return None

def get_manager(user):
    try:
        profile = Profile.objects.get(user=user)
        manager = ManagerInfo.objects.get(profile=profile)
        return manager
    except:
        return None

def get_barista(user):
    try:
        profile = Profile.objects.get(user=user)
        if profile.profile_type == 'BAR':
            return profile
        else: 
            return None
    except:
        return None

def tournament_for_player(player_info):
    return player_info.tournament

def tournament_for_sponsor(sponsor):
    try:
        tournament = Tournament.objects.get(sponsor=sponsor)
        return tournament
    except:
        return None

def determine_redirect_login(user):

    user_type = get_user_type(user)

    if user_type == 'player':
        location = 'index'
    elif user_type == 'barista':
        location = 'barista'  # Redirect baristas to the drinks page
    elif user_type == 'sponsor':
        location = 'sponsor'  # Redirect sponsors to the sponsor page
    else:
        location = 'manager'  # Redirect managers to the manager page

    return location

def get_user_type(user):
    user_type = 'player'

    sponsor = get_sponsor(user)
    manager = get_manager(user)
    barista = get_barista(user)

    if sponsor:
        return 'sponsor'
    elif manager:
        return 'manager'
    elif barista:
        return 'barista'

    return user_type

def get_game_info(user):
    print('getting game info for user...')

    info = get_player(user)['player_info']

    current_score = info.current_score
    current_hole = info.current_hole

    return {'current_score': current_score,'current_hole': current_hole}

def add_stroke_to_player(player, stroke):
    location = 'game'

    profile = player['profile']
    player = player['player_info']

    player.current_hole == 0

    player.current_hole += 1
    player.current_score += int(stroke)

    if player.current_hole > get_number_of_holes():
        location = 'end_game'
        tour = tournament_for_player(player)
        leaderboard = LeaderBoard.objects.create(tournament=tour, profile=profile, score=player.current_score)
        leaderboard.save()

    player.save()

    return location

def get_number_of_holes():
    return VenueInfo.objects.all()[:1].get().number_of_holes

def pay_fee_for_sponsor(user):
    sponsor = get_sponsor(user)
    try: 
        tournament = Tournament.objects.get(sponsor=sponsor)
        tournament.fee_paid = True
        tournament.save()
    except:
        return None

def add_player_to_sponsor(user, player_username):
    sponsor = get_sponsor(user)
    tournament = Tournament.objects.get(sponsor=sponsor)
    
    player_user = User.objects.get(username=player_username)

    player_profile = Profile.objects.get(user=player_user)

    player_info = PlayerInfo.objects.get(profile=player_profile)

    player_info.tournament = tournament
    
    player_info.save()

def get_final_score(user):
    player = get_player(user)['player_info']

    return player.current_score

def get_all_time_leaderboard():
    return LeaderBoard.objects.all().order_by('score')[:50]

def get_leaderboard_for(user):
    tournament = get_player(user)['player_info'].tournament

    return LeaderBoard.objects.filter(tournament=tournament).order_by('score')

def check_game_complete_for(user):
    complete = True

    tournament = get_player(user)['player_info'].tournament

    competitors = PlayerInfo.objects.filter(tournament=tournament)

    for comp in competitors:
        if comp.current_hole <= get_number_of_holes():
            complete = False

    return complete

def set_user_type(to, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)

    profile_type = profile.profile_type

    if to == 'player':
        if profile_type == Profile.ProfileType.PLAYER:
            return
        else: 
            profile.profile_type = Profile.ProfileType.PLAYER
            profile.save()
            try:
                player_info = PlayerInfo.objects.get(profile=profile)
            except:
                # this should likely only happen with our auto generated users that didn't start as players...
                new_info = PlayerInfo.objects.create(profile=profile)
                new_info.save()
    elif to == 'sponsor':
        if profile_type == Profile.ProfileType.SPONSOR:
            return
        else:
            profile.profile_type = Profile.ProfileType.SPONSOR
            profile.save()
            try:
                sponsor_info = SponsorInfo.objects.get(profile=profile)
            except:
                new_info = SponsorInfo.objects.create(profile=profile, title=username)
                new_info.save()
    elif to == 'manager':
        if profile_type == Profile.ProfileType.MANAGER:
            return
        else:
            profile.profile_type = Profile.ProfileType.MANAGER
            profile.save()
            try:
                manager_info = ManagerInfo.objects.get(profile=profile)
            except:
                new_info = ManagerInfo.objects.create(profile=profile, name=username)
                new_info.save()
    else:
        if profile_type == Profile.ProfileType.BARISTA:
            return
        else:
            profile.profile_type = Profile.ProfileType.BARISTA
            profile.save()

def get_user_current_type(username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    return profile.profile_type