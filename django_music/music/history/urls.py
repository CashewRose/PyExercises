from django.urls import path

from . import views
app_name = 'history'
urlpatterns = [
    # ex: /polls/
    path('', views.all_artists, name='all_artists' ),
    path('<int:artist_id>/', views.artist_details, name='artist_details' )
]
