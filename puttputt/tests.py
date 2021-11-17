from django.test import TestCase
import datetime
from django.contrib.auth.models import User, Permission
from .models import PlayerInfo, Profile, DrinkOrder, DrinkInfo, LeaderBoard, Tournament, SponsorInfo

class Unittests(TestCase):
    def setUp(self):
        self.start = datetime.datetime.now()
        self.end = datetime.datetime.now()
        self.user = User.objects.create_user(username="player", password="Testpass1")
        login = self.client.login(username="player", password="Testpass1")
        self.sponsor = User.objects.get(username="sponsor")
        self.spons_prof = Profile.objects.get(user=self.sponsor, profile_type='SPO')
        # login1 = self.client.login(username="sponsor", password="sponsor")
        self.sponsor_info = SponsorInfo.objects.create(profile=self.spons_prof, title="Nike")
        self.profile = Profile.objects.create(user=self.user, profile_type='PLY')
        self.tournament = Tournament.objects.create(sponsor=self.sponsor_info, start_time=self.start, end_time=self.end, fee_paid=True)
        self.player = PlayerInfo.objects.create(profile=self.profile, tournament=self.tournament, current_score=12, current_hole=4, current_funds=23)
        self.drink = DrinkInfo.objects.create(title="Sprite", price=4)
        self.order = DrinkOrder.objects.create(user=self.user, drink=self.drink, quantity=4)

    def testPlayer(self):
        self.assertTrue(self.user != None)
        self.assertTrue(self.user.profile.profile_type, 'PLY')
        self.assertTrue(self.player.tournament != None)
        self.assertTrue(self.player.tournament.sponsor, self.sponsor)
        self.assertTrue(self.player.current_hole, 4)
        self.assertTrue(self.player.current_score, 12)
        self.assertTrue(self.player.current_funds, 23)

    def testTournament(self):
        self.assertTrue(self.tournament != None)
        self.assertTrue(self.tournament.sponsor, self.sponsor_info)
        self.assertTrue(self.tournament.start_time, self.start)
        self.assertTrue(self.tournament.end_time, self.end)
        self.assertTrue(self.tournament.fee_paid, True)

    def testDrink(self):
        self.assertTrue(self.drink != None)
        self.assertTrue(self.drink.title, "Sprite")
        self.assertTrue(self.drink.price, 4)
        self.assertTrue(self.drink.image, "https://tacm.com/wp-content/uploads/2018/01/no-image-available.jpeg")
        self.assertTrue(self.order.user, self.user)
        self.assertTrue(self.order != None)
        self.assertTrue(self.order.drink, self.drink)
        self.assertTrue(self.order.quantity, 4)