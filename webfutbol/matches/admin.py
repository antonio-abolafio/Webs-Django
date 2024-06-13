from django.contrib import admin
from .models import Team, Match

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'shield')
    search_fields = ('name',)

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('journey', 'local_team', 'visiting_team', 'result', 'date')
    search_fields = ('local_team__name', 'visiting_team__name')
    list_filter = ('date', 'journey')
    autocomplete_fields = ('local_team', 'visiting_team')
