'''
    reddit_service.py

    fetches a random til from reddit
    ---------

    usage:
        service = RedditTilService()
        til = service.get_tidbit()
    returns:
        TIL that most of the dogs that have played Lassie are descended from the first dog, named Pal, to play the character. 
        When the first non-blood line dog was given the role in 1997 people protested until producers found another descendent
        to replace it.
'''

import urllib2
import json

class RedditTilService():
    def __init__(self):
        self.url = "https://www.reddit.com/r/todayilearned/random/.json"
        self.headers = { 'User-Agent' : 'Mozilla/5.0' }              

    def get_tidbit(self):
        tidbits = self.get_tidbits()
        return tidbits[0]

    def get_tidbits(self):
        req = urllib2.Request(self.url, None, self.headers)               
        page = urllib2.urlopen(req).read()
        data = json.loads(page)

        tils = unpack_data(data)
        return tils

def unpack_data(data):
    children = data[0]['data']['children']
    tils = [child['data']['title'] for child in children]
    return tils

if __name__ == '__main__':
    service = RedditTilService()
    til = service.get_tidbit()
    print til