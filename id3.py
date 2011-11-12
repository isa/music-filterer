import id3reader

class ID3:
   def __init__(self, file):
      self.id3r = id3reader.Reader(file)

   def artist(self):
      return str(self.id3r.getValue('performer'))

   def album(self):
      return str(self.id3r.getValue('album'))

   def title(self):
      return str(self.id3r.getValue('title'))
