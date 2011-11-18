import os
import unicodedata
import id3reader
from models import *
from pyechonest import config

class ID3(object):
   def __init__(self, path):
      self.path = path
      self.id3r = id3reader.Reader(path)

   def __default__(self, value):
      if value == None:
         full_name = os.path.basename(self.path)
         metadata = os.path.splitext(full_name)[0].split('-')
         return (
            metadata[0].strip().decode('utf-8'),
            u'',
            metadata[1].strip().decode('utf-8')
         )
      return (value, value, value) # this is for any kind like whether it is artist or title or whatever..

   def artist(self):
      return self.__default__(self.id3r.getValue('performer'))[0]
      # return unicodedata.normalize('NFKD', value).encode('ascii','ignore')

   def album(self):
      return self.__default__(self.id3r.getValue('album'))[1]
      # return unicodedata.normalize('NFKD', value).encode('ascii','ignore')

   def title(self):
      return self.__default__(self.id3r.getValue('title'))[2]
      # return unicodedata.normalize('NFKD', value).encode('ascii','ignore')

class FileBrowser(object):
   def __init__(self, path):
      self.path = path

   def __list_mp3_files_under__(self, path):
      mp3_files = []
      for item in os.listdir(path):
         full_name = os.path.join(path, item)

         if (os.path.isfile(full_name)):
            extension = os.path.splitext(full_name)[1][1:]

            if (extension.lower() == 'mp3'): mp3_files.append(full_name)
         else:
            mp3_files.extend(self.__list_mp3_files_under__(full_name))

      return mp3_files

   def all_files(self):
      return self.__list_mp3_files_under__(self.path)

class SongDatabase(object):
   def __create_artist_with__(self, name):
      artist = STORE.find(Artist, Artist.name == name).one()

      if artist == None:
         artist = Artist()
         artist.name = name
         artist = STORE.add(artist)
         STORE.commit()

      return artist

   def __create_song_with__(self, artist_id, album, title):
      song = STORE.find(Song, Song.artist_id == artist_id, Song.album == album, Song.title == title).one()

      if song == None:
         song = Song()
         song.artist_id = artist_id
         song.album = album
         song.title = title
         song.time_signature = 0
         song.key = 0
         song.minor_major = 0
         song.energy = 0.0;
         song.tempo = 0.0;
         song.danceability = 0.0;
         song.loudness = 0.0;
         song.duration = 0.0;
         song = STORE.add(song)
         STORE.commit()

      return song

   def create_from(self, path):
      all_files = FileBrowser(path).all_files()

      for file_name in all_files:
         id3 = ID3(file_name)
         artist = self.__create_artist_with__(id3.artist())
         song = self.__create_song_with__(artist.id, id3.album(), id3.title())
         print "%s - %s" % (artist.name, song.title)


class TasteFinder(object):
   def __init__(self, five_star_likes, four_star_likes):
      config.ECHO_NEST_API_KEY = "TA4OHCAV5FQCJTWVJ"
      self.five_star_likes = five_star_likes
      self.four_star_likes = four_star_likes


