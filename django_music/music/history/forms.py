from django import forms

class AlbumForm(forms.Form):
    album_name = forms.CharField(label='Name of the Album', max_length=25)
    artist_name = forms.CharField(label='Name of Artist', max_length=25)