from pyechonest import config
from utils import ID3
from utils import FileBrowser

config.ECHO_NEST_API_KEY = "TA4OHCAV5FQCJTWVJ"

if (__name__ == "__main__"):
   print "Will be filtering.."

   for file_name in FileBrowser('/Users/isa/Music').all_files():
      id = ID3(file_name)
      print "%s - %s" % (id.artist(), id.title())
