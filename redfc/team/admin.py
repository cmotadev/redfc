from django.contrib import admin
from .models import Team, TeamManager

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(TeamManager)
class TeamManagerAdmin(admin.ModelAdmin):
    pass