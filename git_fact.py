import sys
sys.path.append('Snapple')

from termcolor import colored
from snapple_service import *

service = SnappleFactService()
tidbit = service.get_tidbit()

print ""
print (tidbit, 'green')
