from storm.locals import *

DATABASE = create_database('sqlite:data/library.db')
STORE = Store(DATABASE)

class Artist(object):
   __storm_table__ = 'artist'
   id = Int(primary = True)
   name = Unicode()

class Song(object):
   __storm_table__ = 'song'
   id = Int(primary = True)
   album = Unicode()
   title = Unicode()
   time_signature = Int()
   minor_major = Bool()
   key = Int()
   energy = Float()
   tempo = Float()
   danceability = Float()
   loudness = Float()
   duration = Float()
   artist_id = Int()
   artist = Reference(artist_id, Artist.id)

class Term(object):
   __storm_table__ = 'term'
   id = Int(primary = True)
   value = Unicode()
   artist_id = Int()
   artist = Reference(artist_id, Artist.id)

class Mood(object):
   __storm_table__ = 'mood'
   id = Int(primary = True)
   value = Unicode()
   artist_id = Int()
   artist = Reference(artist_id, Artist.id)

