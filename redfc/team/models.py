from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Team(models.Model):
    name = models.CharField(
        max_length=100,
    )

    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.name


class TeamManager(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} <{self.team.name}>"