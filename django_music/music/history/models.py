from django.db import models

# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length=50)

class Album(models.Model):
    album_name = models.CharField(max_length=50)
    album_artist = models.ForeignKey(Artist, on_delete=models.PROTECT)

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=50)
    song_album = models.ForeignKey(Album, on_delete=models.PROTECT)
