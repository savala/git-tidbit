# something
import sys
sys.path.append('Snapple')

from snapple_service import *

service = SnappleFactService()
tidbit = service.get_tidbit()
print tidbit
