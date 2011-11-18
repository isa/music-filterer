from utils import *

if (__name__ == "__main__"):
   print "Will be filtering.."

   5stars = [('John Mayer', 'Say'), ('Train', 'Hey, Soul Sister'), ('Jason Mraz', "I'm Yours"), ('Jashua Radin', 'Paperweight'), ('Rodrigo y Gabriela', 'Tamacun'), ('Johnny Cash', 'Solitary Man')]
   4stars = [('Gotye', 'Coming Back'), ('Jack Johnson', 'Sexy Plexi'), ('Miss Li', 'Let Her Go'), ('Nick Drake', 'Three Hours'), ('Tomas Lozano', 'Las Tres Mozuelas'), ('Vampire Weekend', 'Mansard Roof')]

   taste_finder = TasteFinder(5stars, 4stars)
   print taste_finder.__keys__()

   for file_name in FileBrowser('/Users/isa/Music/Misc').all_files():
      id = ID3(file_name)
      print "%s - %s" % (id.artist(), id.title())
