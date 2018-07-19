
from django.db import models

# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length=200)


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=200)
