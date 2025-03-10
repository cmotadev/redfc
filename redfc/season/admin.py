from django.contrib import admin
from .models import Season, MatchField, Match, MatchResult

# Register your models here.
@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ["name", "start_date", "end_date"]


@admin.register(MatchField)
class MatchFieldAdmin(admin.ModelAdmin):
    list_display = ["name", "address"]


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ["contestant", "field", "home_or_away", "schedule", "cancelled"]
    list_filter = ["season"]

@admin.register(MatchResult)
class MatchResultAdmin(admin.ModelAdmin):
    list_display = ["match", "home_goals", "away_goals", "get_result_display"]
    list_filter = ["match__season"]