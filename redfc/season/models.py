from django.db import models
from ..team.models import Team

# Create your models here.
class Season(models.Model):
    """
    Temporada
    """
    name = models.CharField(
        max_length=100,
        blank=True
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.RESTRICT
    )

    start_date = models.DateField()

    end_date = models.DateField()

    def __str__(self):
        _name = self.name if self.name else "Unnamed season"
        return f"{_name} <{self.team.name}>"


class MatchField(models.Model):
    """
    Campo de jogo
    """
    name = models.CharField(
        max_length=100
    )

    slug = models.SlugField(
        max_length=100
    )

    address = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.name


class Match(models.Model):
    """
    Partida
    """
    class MatchLocation(models.TextChoices):
        HOME = ("h", "Home")
        AWAY = ("a", "Away")
    
    season = models.ForeignKey(
        Season,
        models.RESTRICT,
        limit_choices_to=models.Q(start_date__lte=models.F('end_date')) & models.Q(end_date__gte=models.F('start_date'))
    )

    field = models.ForeignKey(
        MatchField,
        on_delete=models.RESTRICT
    )

    home_or_away = models.CharField(
        max_length=1,
        choices=MatchLocation.choices
    )

    schedule = models.DateTimeField()

    contestant = models.CharField(
        max_length=100
    )

    cancelled = models.BooleanField(
        default=False
    )

    notes = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name_plural = "matches"
        unique_together = ("season", "schedule")

    def __str__(self):
        contestants = (self.season.team.name, self.contestant)
        if self.home_or_away == self.MatchLocation.AWAY:
            contestants = reversed(contestants)
        return "{} x {}".format(*contestants)


class MatchResult(models.Model):
    """
    Resultado do jogo
    """
    match = models.OneToOneField(
        Match,
        on_delete=models.CASCADE,
        limit_choices_to=models.Q(cancelled=False),
        primary_key=True
    )

    home_goals = models.PositiveSmallIntegerField(
        default=0
    )

    away_goals = models.PositiveSmallIntegerField(
        default=0
    )

    notes = models.TextField(
        blank=True
    )

    def get_result_display(self):
        return f"{self.home_goals} x {self.away_goals}"
    
    get_result_display.short_description = "final result"

    def __str__(self):
        return f"{self.match} [{self.get_result_display()}]"
