import sys, random
from termcolor import colored

sys.path.append('Snapple')
sys.path.append('Reddit')
from snapple_service import *
from reddit_service import *

if (random.random() < 0.5):
    service = SnappleFactService()
else:
    service = RedditTilService()

tidbit = service.get_tidbit()

print ""
print colored(tidbit, 'green')
