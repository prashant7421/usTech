from django.db import models
import datetime
from django_countries.fields import CountryField


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Team(BaseModel):
    name = models.CharField(max_length=50)
    logo = models.ImageField(blank=True, upload_to='team_logo/')
    club_or_state = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.name).capitalize()




class Player(BaseModel):
    first_name = models.CharField(max_length=20)
    last_name =models.CharField(max_length=20, default='')
    image = models.ImageField(blank=True, upload_to='players/')
    jersey_no = models.IntegerField(blank=True)
    country = CountryField()

    def __str__(self):
        return str(self.first_name).capitalize() + ' ' + str(self.last_name).capitalize()


class Match(BaseModel):
    team1 = models.ForeignKey(
        Team, on_delete=models.ProtectedError, verbose_name="Select Team 1", related_name="team1")
    team2 = models.ForeignKey(
        Team, on_delete=models.ProtectedError, verbose_name="Select Team 2", related_name='team2')
    title = models.CharField(max_length=20, default='')
    match_date = models.DateTimeField()
    team1_score = models.IntegerField(default=0)
    team1_wicket = models.IntegerField(default=0)
    team1_overs = models.DecimalField(default=0.0, decimal_places=3, verbose_name="Overs Played by Team1", max_digits=10)
    team2_score = models.IntegerField(default=0)
    team2_wicket = models.IntegerField(default=0)
    team2_overs = models.DecimalField(default=0.0, decimal_places=3, verbose_name = "Overs Played by Team2", max_digits=10)
    winner =  models.ForeignKey(Team, on_delete=models.ProtectedError, verbose_name="Winner", related_name='Winner', null=True)
    draw = models.BooleanField(default=False)


    def __str__(self):
        return self.team1.name + ' vs ' + self.team2.name + ' (' + self.title +')'

    



class MatchPlayers(BaseModel):
    match = models.ForeignKey(
        Match, on_delete=models.ProtectedError, verbose_name="Select Match")
    team = models.ForeignKey(
        Team, on_delete=models.ProtectedError, verbose_name="Select Team")
    player = models.ForeignKey(
        Player, on_delete=models.ProtectedError, verbose_name="Select Player")
   


    class Meta:
        unique_together = ('match','team', 'player')

    def __str__(self):
        return str(self.player.first_name).capitalize() + ' ' + str(self.player.last_name).capitalize()+ '  from ' +self.team.name + ' ' + '(' + self.match.team1.name + ' vs ' + self.match.team2.name + '->' + self.match.title + ')'

class PlayerStatistics(BaseModel):
    match_player = models.OneToOneField(MatchPlayers, on_delete=models.ProtectedError, verbose_name="Select Player")
    run = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    catches = models.IntegerField(default=0)
    balls_played = models.FloatField(default=0.0, verbose_name='Balls')
    bowling_over = models.IntegerField(default=0)


    def __str__(self):
        return str(self.match_player.player.first_name).capitalize() + ' ' + str(self.match_player.player.last_name).capitalize() + ' (' + self.match_player.team.name + ')'





