from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Artist, Song, Album
from django.urls import reverse


from .forms import AlbumForm

# Using a class-based genric view especially for rendering forms
from django.views.generic.edit import FormView
from django.views.generic import ListView, TemplateView

class SearchView(FormView):
  template_name = 'music/albums.html'
  form_class = AlbumForm

  def album_artist_stuff(self):
    artist_list = Artist.objects.order_by('-id')
    album_list = Album.objects.order_by('-id')
    context = {'artist_list': artist_list,
    'album_list': album_list}
    return context

class CollectionView(TemplateView):
    template_name = 'collection_list.html'

    # Don't need to do this any more, it seems!
    # def get_context_data(self, **kwargs):
    #   # Call the base implementation first to get a context
    #   context = super().get_context_data(**kwargs)
    #   # Get the data from the API
    #   search_results = form.search()
    #   # Add in a QuerySet of the collection data
    #   context['collection'] = search_results
    #   return context
    # Because now you can define values that become props of a new 'view' object in the template
    # https://reinout.vanrees.org/weblog/2014/05/19/context.html
    def collection(self): #NOTE that it's the method name that becomes the property on 'view'
      games = ApiService.get_collection(username=self.request.GET.get('username'))
      print("games", games)
      return games

    def message(self):
      test = {"header": "this is really cool!"}
      return test






def all_artists(request):
    artist_list = Artist.objects.order_by('-id')[:5]
    album_list = Album.objects.order_by('-id')
    context = {'artist_list': artist_list,
    'album_list': album_list}
    return render(request, 'music/album.html', context)

def artist_details(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'music/songs.html', {'artist': artist})
