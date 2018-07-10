# Example set
songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Nickelback', 'Animals'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight')
}

killing_nickelback_songs = { good_song for good_song in songs if good_song[0] is not "Nickelback"}

print(killing_nickelback_songs)
