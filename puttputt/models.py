from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# each user will have a record in Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # a profile can be a player, manager, barista, or sponsor
    class ProfileType(models.TextChoices):
        PLAYER = 'PLY', _('Player')
        MANAGER = 'MAN', _('Manager')
        BARISTA = 'BAR', _('Barista')
        SPONSOR = 'SPO', _('Sponsor')
    
    # this is actually where the player field is setup!
    profile_type = models.CharField(
        max_length=3,
        choices=ProfileType.choices,
        # new profiles are automatically a PLAYER
        default=ProfileType.PLAYER,
    )

class SponsorInfo(models.Model):
    # the profile for this sponsor
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # the title of the sponsor: i.e. Nike
    title = models.CharField(max_length=50)

class Tournament(models.Model):
    # who sponsored the event
    sponsor = models.ForeignKey(SponsorInfo, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # once the fee has been paid a tournament can begin
    fee_paid = models.BooleanField(default=False)

# Extended User Information
class PlayerInfo(models.Model):
    # the player's profile
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # what tournament the player is allowed to play in 
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)
    # the player's current score (update this after each stroke)
    current_score = models.IntegerField(default=0)
    # the player's current hole (update this after each stroke)
    current_hole = models.IntegerField(default=0)

class ManagerInfo(models.Model):
    # the profile of this Manager
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # the manager's name
    name = models.CharField(max_length=50)
    # how much cash this manager has in the register that has not yet been payed to the owner
    cash_on_hand = models.IntegerField(default=0)


class DrinkInfo(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()

class LeaderBoard(models.Model):
    # what tournament the score belongs to
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    # who scored this
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # what the score was
    score = models.IntegerField()

class Prizes(models.Model):
    title = models.CharField(max_length=50)
    # how much the prize is worth
    value = models.IntegerField()
    # what place on the leaderboard they must get to win this prize. defaults 1 2 and 3
    place_to_win = models.IntegerField()

class DrinkOrder(models.Model):
    # who ordered the drink
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # which drink was ordered
    drink = models.ForeignKey(DrinkInfo, on_delete=models.CASCADE)
    # whether or not the drink has been delivered
    order_delivered = models.BooleanField(default=False)

class VenueInfo(models.Model):
    title = models.CharField(max_length=50)
    number_of_holes = models.IntegerField()

