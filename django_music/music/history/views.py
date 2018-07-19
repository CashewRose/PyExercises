from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Artist, Song
from django.urls import reverse

def all_artists(request):
    artist_list = Artist.objects.order_by('-id')[:5]
    context = {'artist_list': artist_list}
    return render(request, 'music/artists.html', context)

def artist_details(request, artist_id):
    print(artist_id)
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'music/songs.html', {'artist': artist})
