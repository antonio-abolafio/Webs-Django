from django.contrib import admin
from .models import Position, Player, Statistic
from .forms import StatisticForm


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)



@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'soccer_number', 'position')
    search_fields = ('name', 'last_name', 'alias', 'soccer_number', 'position')
    list_filter = ('position',)
    readonly_fields = ('age', 'slug')


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    form = StatisticForm
    list_display = ('player',)
    search_fields = ('player__name', 'player__last_name', 'player__alias', 'player__soccer_number', 'player__position')
    list_filter = ('minutes_played', 'goals', 'yellow_cards', 'red_cards')
