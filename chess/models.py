from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from.choices import *

# Create your models here.

class Author(models.Model):
    forename = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    created_on = models.DateTimeField(default=timezone.now)


class Tag(models.Model):
    name = models.CharField(max_length=32)


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Player(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    rating = models.IntegerField(default=800)
    nationality = CountryField()
    created_on = models.DateTimeField(default=timezone.now)


class Game(models.Model):
    white_player = models.ForeignKey(
        Player, 
        on_delete=models.CASCADE,
        related_name="white_player"
    )
    black_player = models.ForeignKey(
        Player, 
        on_delete=models.CASCADE,
        related_name="black_player"
    )
    result = models.IntegerField(choices=GAME_RESULT_CHOICES)
    ranked = models.BooleanField()
