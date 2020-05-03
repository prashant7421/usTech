from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from cricket import models
from django.contrib import messages
from django.db.models import ProtectedError

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','logo','club_or_state',)
    list_filter = ('name','club_or_state',)
    search_fields = ('name', 'club_or_state',)

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super().delete_view(request, object_id, extra_context)
        except (ProtectedError, TypeError) as e:
            msg = "you cannot hard delete this Team, It has some dependency"
            self.message_user(request, msg, messages.ERROR)
            opts = self.model._meta
            return_url = reverse(
                'admin:%s_%s_change' % (opts.app_label, opts.model_name),
                args=(object_id,),
                current_app=self.admin_site.name,
            )
            return HttpResponseRedirect(return_url)

    def response_action(self, request, queryset):
        try:
            return super().response_action(request, queryset)
        except (ProtectedError, TypeError) as e:
            msg = "you cannot hard delete this Team, It has some dependency"
            self.message_user(request, msg, messages.ERROR)
            opts = self.model._meta
            return_url = reverse(
                'admin:%s_%s_changelist' % (opts.app_label, opts.model_name),
                current_app=self.admin_site.name,
            )
            return HttpResponseRedirect(return_url)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'image', 'jersey_no', 'country',)
    list_filter = ('first_name', 'last_name', 'jersey_no', 'country',)
    search_fields = ('first_name', 'last_name', 'jersey_no', 'country',)

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super().delete_view(request, object_id, extra_context)
        except (ProtectedError, TypeError) as e:
            msg = "you cannot hard delete this Player, It has some dependency"
            self.message_user(request, msg, messages.ERROR)
            opts = self.model._meta
            return_url = reverse(
                'admin:%s_%s_change' % (opts.app_label, opts.model_name),
                args=(object_id,),
                current_app=self.admin_site.name,
            )
            return HttpResponseRedirect(return_url)

    def response_action(self, request, queryset):
        try:
            return super().response_action(request, queryset)
        except (ProtectedError, TypeError) as e:
            msg = "you cannot hard delete this Player, It has some dependency"
            self.message_user(request, msg, messages.ERROR)
            opts = self.model._meta
            return_url = reverse(
                'admin:%s_%s_changelist' % (opts.app_label, opts.model_name),
                current_app=self.admin_site.name,
            )
            return HttpResponseRedirect(return_url)


class MatchAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2',
                    'title', 'match_date', 'team1_score', 'team1_wicket', 'team2_score', 'team2_wicket', 'winner', 'draw', 'team1_overs', 'team2_overs',)
    list_filter = ('team1', 'team2',
                   'title', 'match_date',  'winner', 'draw',)
    search_fields = ('team1', 'team2',
                     'title', 'match_date',  'winner', 'draw',)

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super().delete_view(request, object_id, extra_context)
        except (ProtectedError, TypeError) as e:
            msg = "you cannot hard delete this Match, It has some dependency"
            self.message_user(request, msg, messages.ERROR)
            opts = self.model._meta
            return_url = reverse(
                'admin:%s_%s_change' % (opts.app_label, opts.model_name),
                args=(object_id,),
                current_app=self.admin_site.name,
            )
            return HttpResponseRedirect(return_url)

    def response_action(self, request, queryset):
        try:
            return super().response_action(request, queryset)
        except (ProtectedError, TypeError) as e:
            msg = "you cannot hard delete this Match, It has some dependency"
            self.message_user(request, msg, messages.ERROR)
            opts = self.model._meta
            return_url = reverse(
                'admin:%s_%s_changelist' % (opts.app_label, opts.model_name),
                current_app=self.admin_site.name,
            )
            return HttpResponseRedirect(return_url)


class MatchPlayersAdmin(admin.ModelAdmin):
    list_display = ('match', 'team',
                    'player',)
    list_filter = ('match', 'team',
                   'player',)
    search_fields = ('match', 'team',
                     'player',)

    def delete_view(self, request, object_id, extra_context=None):
        try:
            return super().delete_view(request, object_id, extra_context)
        except (ProtectedError, TypeError) as e:
            msg = "you cannot hard delete this Player from this match, It has some dependency from statistics"
            self.message_user(request, msg, messages.ERROR)
            opts = self.model._meta
            return_url = reverse(
                'admin:%s_%s_change' % (opts.app_label, opts.model_name),
                args=(object_id,),
                current_app=self.admin_site.name,
            )
            return HttpResponseRedirect(return_url)

    def response_action(self, request, queryset):
        try:
            return super().response_action(request, queryset)
        except (ProtectedError, TypeError) as e:
            msg = "you cannot hard delete this Player from this match, It has some dependency from statistics"
            self.message_user(request, msg, messages.ERROR)
            opts = self.model._meta
            return_url = reverse(
                'admin:%s_%s_changelist' % (opts.app_label, opts.model_name),
                current_app=self.admin_site.name,
            )
            return HttpResponseRedirect(return_url)


class PlayersStatisticsAdmin(admin.ModelAdmin):
    list_display = ('match_player', 'run',
                    'wickets', 'catches', 'balls_played', 'bowling_over',)
    list_filter = ('match_player',)
    search_fields = ('match_player',)


admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.Player, PlayerAdmin)
admin.site.register(models.Match, MatchAdmin)
admin.site.register(models.MatchPlayers, MatchPlayersAdmin)
admin.site.register(models.PlayerStatistics, PlayersStatisticsAdmin)

admin.site.site_header = "USTech Solutions (username - ustech and password - ustech@4321)"
admin.site.site_title = "USTech Solutions"
admin.site.index_title = "USTech Solutions"


   
