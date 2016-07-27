'''
    snapple_service.py

    fetches a random fact from snapple
    ---------

    usage:
        from gittidbit import snapple_service
        snapple_service.get_tidbit()
    returns:
        You burn about 20 calories per hour chewing gum.
'''

from bs4 import BeautifulSoup
import urllib2

headers = { 'User-Agent' : 'Mozilla/5.0' }
url  = 'http://www.snapple.com/real-facts/cap-view'


def get_tidbit():
    facts = get_tidbits()
    return facts[0]

def get_tidbits():
    req = urllib2.Request(url, None, headers)
    html = urllib2.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')

    titleTag = soup.find("title").string
    p_soup   = soup.findAll('p')
    p_info   = [p.string for p in p_soup]

    more_facts_tags = soup.findAll("div", { "class" : "fact_text_wrap" })
    more_facts_strs = [div.find('p').string for div in more_facts_tags]

    return more_facts_strs


if __name__=='__main__':
    fact = get_tidbit()
    print fact