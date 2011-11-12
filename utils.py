import os
import unicodedata
import id3reader

class ID3:
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
      value = self.__default__(self.id3r.getValue('performer'))[0]
      return unicodedata.normalize('NFKD', value).encode('ascii','ignore')

   def album(self):
      value = self.__default__(self.id3r.getValue('album'))[1]
      return unicodedata.normalize('NFKD', value).encode('ascii','ignore')

   def title(self):
      value = self.__default__(self.id3r.getValue('title'))[2]
      return unicodedata.normalize('NFKD', value).encode('ascii','ignore')

class FileBrowser:
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

