from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from history.models import Song, Artist, Album

class Command(BaseCommand):

  def handle(self, *args, **options):
    seeder.add_entity(Artist, 15, {'artist_name': lambda x: seeder.faker.name()})
    # Override the seeder "guess" of what faker provider you want it to use
    seeder.add_entity(Album, 40, {'album_name': lambda x: seeder.faker.catch_phrase()})
    seeder.add_entity(Song, 40, {'song_name': lambda x: seeder.faker.catch_phrase()})

    inserted_pks = seeder.execute()