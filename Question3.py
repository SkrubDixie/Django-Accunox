from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Artist(models.Model):
    name = models.CharField()

class Song(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Artist)

# Signal handler to create a song when an artist is created
@receiver(post_save, sender=Artist)
def create_book(sender, instance, created, **kwargs):
    if created:
        Song.objects.create(title='New Song', artist=instance)
        # This will run in the same transaction as artist creation

# Creating an artist to trigger the signal
artist = Artist.objects.create(name='Shubham')

# Printing the song title
song = Song.objects.filter(title='New Song').first()
print(song.title)

# This will create a song whenever a new artist is created
# It demonstrates that signals run in the same database transaction as caller