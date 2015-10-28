import urllib2
from bs4 import BeautifulSoup
import time

actorSite = urllib2.urlopen('http://www.imdb.com/search/name?birth_monthday=01-28')
actorHTML = actorSite.read()
actorSite.close()
actorSoup = BeautifulSoup(actorHTML, 'lxml')

actorNames = actorSoup.select('.name > a')

for actor in actorNames:
    print actor.get_text()
    print 'www.imdb.com/'+actor.get("href")

