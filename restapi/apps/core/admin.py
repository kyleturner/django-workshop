from django.contrib import admin

from apps.core.models import *

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'mascot')
    search_fields = ('name', 'city', 'mascot')
    prepopulated_fields = {'slug': ('name', )}
    model = Team

class PlayerAdmin(admin.ModelAdmin):
    model = Player
    
admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)