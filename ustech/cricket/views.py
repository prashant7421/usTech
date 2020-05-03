from django.shortcuts import render
from cricket.models import Team, Match, MatchPlayers, Player, PlayerStatistics
from django.http import Http404
from django.views import View
from django.db.models import Q
from django.db.models import Sum



class Index(View):

    def get(self, request):
        allTeams = Team.objects.all()
        teamWithPlayers = self.getTeamsWithPlayers(allTeams)
        allMatches = self.getAllMatches()
        pointsTable  = self.getPointsTable(allTeams)
        return render(request, 'home.html',{'teams': teamWithPlayers, 'matches':allMatches,'p_table':pointsTable})
        
    def getTeamsWithPlayers(self, allTeams):
        teamWithPlayers = []
        if allTeams:
            for team in allTeams:
                tempDict = {}
                players = MatchPlayers.objects.filter(team=team)
                tempDict['team'] = team
                tempDict['players'] = players
                teamWithPlayers.append(tempDict)
        return teamWithPlayers

    def getAllMatches(self):
        allMatches = Match.objects.all().order_by('match_date')
        return allMatches

    def getPointsTable(self, allTeams):
        pointsTable = []
        if allTeams:
            for team in allTeams:
                teamData = {}
                matchPlayed = Match.objects.filter(
                    (Q(team1=team) | Q(team2=team)), Q(draw=True) | ~Q(winner=None)).count()
                matchWon = Match.objects.filter(winner=team).count()
                matchDraw = Match.objects.filter((Q(team1=team) | Q(team2=team)),Q( draw=True)).count()
                matchLost = matchPlayed - (matchWon+matchDraw)
                nRR = self.calulateNRR(team)
                points = self.calculatePoints(matchWon, matchDraw)
                teamData['team'] = team
                teamData['played'] = matchPlayed
                teamData['won'] = matchWon
                teamData['draw'] = matchDraw
                teamData['lost'] = matchLost
                teamData['nrr'] = round(nRR, 3)
                teamData['points'] = points
                pointsTable.append(teamData)

        return pointsTable

                
                

            
    def calculatePoints(self, won, draw):
        a = won * 2
        a = a + draw
        return a

    def calulateNRR(self, team):
        ownRR = 0
        againstRR = 0
        ownR, againstR = self.calculateTotalRuns(team)
        ownO, againstO = self.calculateTotalOvers(team)

        if ownO > 0:
            ownRR = ownR/ownO

        if againstO > 0:
            againstRR = againstR/againstO
        
        nRR = ownRR - againstRR
        return nRR

    def calculateTotalRuns(self, team):
        a = Match.objects.filter(team1=team).aggregate(
            Sum('team1_score'))['team1_score__sum']
        try:
            a = int(a)
        except (ValueError, TypeError) as error:
            a = 0
        
        b = Match.objects.filter(team2=team).aggregate(
            Sum('team2_score'))['team2_score__sum']

        try:
            b = int(b)
        except (ValueError, TypeError) as error:
            b = 0
        
       

        e = Match.objects.filter(team1=team).aggregate(
            Sum('team2_score'))['team2_score__sum']

        try:
            e = int(e)
        except (ValueError, TypeError) as error:
            e = 0

        f = Match.objects.filter(team2=team).aggregate(
            Sum('team1_score'))['team1_score__sum']

        try:
            f = int(f)
        except (ValueError, TypeError) as error:
            f = 0

        c =  a + b
        g = e + f
        return c, g

    def calculateTotalOvers(self, team):
        a = Match.objects.filter(team1=team).aggregate(
            Sum('team1_overs'))['team1_overs__sum']

        try:
            a = float(a)
        except (ValueError, TypeError) as error:
            a = 0

        b = Match.objects.filter(team2=team).aggregate(
            Sum('team2_overs'))['team2_overs__sum']

        try:
            b = float(b)
        except (ValueError, TypeError) as error:
            b = 0

        e = Match.objects.filter(team1=team).aggregate(
            Sum('team2_overs'))['team2_overs__sum']

        try:
            e = float(e)
        except (ValueError, TypeError) as error:
            e = 0

        f = Match.objects.filter(team2=team).aggregate(
            Sum('team1_overs'))['team1_overs__sum']

        try:
            f = float(f)
        except (ValueError, TypeError) as error:
            f = 0

        c = a + b
        g = e + f
        return c, g


class PlayerProfile(View):

    def get(self,request, id):
        try:
            
            player = Player.objects.filter(id=id)[0]
            print(player)
            a = PlayerStatistics.objects.filter(match_player__player=player).aggregate(
                Sum('run'))['run__sum']

            w = PlayerStatistics.objects.filter(match_player__player=player).aggregate(
                Sum('wickets'))['wickets__sum']

            c = PlayerStatistics.objects.filter(match_player__player=player).aggregate(
                Sum('catches'))['catches__sum']

            try:
                a = int(a)
            except (ValueError, TypeError) as error:
                a = 0

            try:
                w = int(w)
            except (ValueError, TypeError) as error:
                w = 0

            try:
                c = int(c)
            except (ValueError, TypeError) as error:
                c = 0

            hundreds = PlayerStatistics.objects.filter(
                Q(match_player__player=player), Q(run__gte = 100)).count()

            fifties = PlayerStatistics.objects.filter(
                Q(match_player__player=player), Q(run__gte = 50), Q(run__lt = 100)).count()
            return render(request, 'player_profile.html', {'player': player, 'run': a, 'wickets': w, 'catches': c, 'fifties': fifties, 'hundreds': hundreds})

        except Player.DoesNotExist:
            return Http404
        return Http404
        



    
