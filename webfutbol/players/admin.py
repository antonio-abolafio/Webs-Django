from django.contrib import admin
from .models import Player, Statistic


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'soccer_number', 'age')
    search_fields = ('name', 'last_name', 'soccer_number')
    list_filter = ('soccer_number',)
    readonly_fields = ('age',)


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('player',)
    search_fields = ('player',)
    list_filter = ('goals',)